using System.Collections;
using System.Collections.Specialized;

namespace Algorithms.MostWordyUsers
{
    class Solution
    {
        public string Filename { get; }
        public int UsersNbr { get; }

        public Solution(string filename, int usersNbr)
        {
            this.Filename = filename;
            this.UsersNbr = usersNbr;
        }

        public IDictionary Run()
        {
            var dic = new OrderedDictionary();
            foreach (var (username, wordcount) in RunPriorityQueue())
            {
                dic[username] = wordcount;
            }

            return dic;
        }

        public IEnumerable<(string username, int wordcount)> RunPriorityQueue()
        {
            var usersToWords = new Dictionary<string, int>();
            var usersList = new PriorityQueue<(string, int), int>();
            Console.WriteLine($"Parsing {this.Filename} for top {this.UsersNbr} users!");

            IEnumerable<(string username, int wordcount)> ParseItr(string filename)
            {
                var fs = File.OpenRead(filename);
                try
                {
                    var sr = new StreamReader(fs);
                    try
                    {
                        string? line;
                        do
                        {
                            line = sr.ReadLine();

                            if (Line.TryParse(line ?? string.Empty, out Line l))
                            {
                                yield return (l.Username, l.Wordcount);
                            }

                        }
                        while (line != null);

                    }
                    finally
                    {
                        sr.Dispose();
                    }
                }
                finally
                {
                    fs.Dispose();
                }
            }

            foreach (var (username, wordcount) in ParseItr(this.Filename))
            {
                usersToWords.TryGetValue(username, out int wordcountOld);
                usersToWords[username] = wordcountOld + wordcount;
            }

            foreach (var line in usersToWords)
            {
                if (usersList.Count < this.UsersNbr)
                {
                    usersList.Enqueue((line.Key, line.Value), line.Value);
                }
                else
                {
                    var (username, wordcount) = usersList.Peek();
                    if (wordcount < line.Value)
                    {
                        usersList.Dequeue();
                        usersList.Enqueue((line.Key, line.Value), line.Value);
                    }
                }
            }

            foreach (var ((username, _), wordcount) in usersList.UnorderedItems.OrderByDescending(x=> x.Priority))
            {
                Console.WriteLine($"{username} user typed {wordcount} words");
                yield return (username, wordcount);
            }
        }
    }
}