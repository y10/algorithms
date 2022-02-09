var env = MyEnvironment.Parse(args);
var usersToWords = new System.Collections.Generic.Dictionary<string, int>();
var usersList = new System.Collections.Generic.PriorityQueue<(string, int), int>();
Console.WriteLine($"Parsing {env.Filename} for top {env.UsersNbr} chatty users!");

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

foreach (var (username, wordcount) in ParseItr(env.Filename))
{
    usersToWords.TryGetValue(username, out int wordcountOld);
    usersToWords[username] = wordcountOld + wordcount;
}

foreach (var line in usersToWords)
{
    if (usersList.Count < env.UsersNbr)
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

foreach (var (username, wordcount) in usersList.UnorderedItems)
{
    Console.WriteLine($"{username} user typed {wordcount} words");
}
