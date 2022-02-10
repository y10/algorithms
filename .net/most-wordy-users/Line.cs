namespace Algorithms.MostWordyUsers
{
    public struct Line
    {
        public static Line Undefined = new Line();
        public int Wordcount;

        public string Username;

        static bool ParseUsername(string line, out string username)
        {
            int startIndex = line.IndexOf('<');
            if (startIndex == -1)
            {
                username = string.Empty;
                return false;
            }

            int endIndex = line.IndexOf('>');
            username = line.Substring(startIndex + 1, endIndex - startIndex - 1);
            return true;
        }

        static int CountASCYWords(string line)
        {

            return 0;
        }

        static int CountSpaceDelemitedWords(string line)
        {
            int startIndex = line.IndexOf('"');
            if (startIndex == -1)
                return 0;

            int endIndex = line.LastIndexOf('"');
            if (endIndex == -1)
                return 0;

            if (endIndex == startIndex)
                return 0;

            int wordcount = 1;
            for (int i = startIndex + 1; i < endIndex; i++)
            {
                char c = line[i];

                for (; i < endIndex && line[i] != ' '; i++)
                {
                    // find word ending
                }

                if (i < endIndex)
                {
                    wordcount++;
                }

                for (; i < endIndex && line[i] == ' '; i++)
                {
                    // find next word befining
                }
            }

            return wordcount;
        }

        public static bool TryParse(string str, out Line line)
        {

            if (!ParseUsername(str, out string username))
            {
                line = Line.Undefined;
                return false;
            }

            line = new Line
            {
                Username = username,
                Wordcount = CountSpaceDelemitedWords(str)
            };

            return true;
        }
    }
}