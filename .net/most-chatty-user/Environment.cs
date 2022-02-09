public class MyEnvironment
{
    static int ParseUsersNbr(String[] args)
    {
        if (args.Length == 0)
        {
            return 0;
        }

        return Convert.ToInt32(args[1]);
    }

    static string ParseFilename(String[] args)
    {
        if (args.Length == 0)
        {
            return "";
        }

        return args[0];
    }

    public static MyEnvironment Parse(String[] args)
    {
        if (args.Length == 0)
        {
            throw new ArgumentException("Please enter a file name and number of usesr to select.");
        }

        return new MyEnvironment
        (
            filename: ParseFilename(args),
            usersNbr:  ParseUsersNbr(args)
        );
    }

    public MyEnvironment(string filename, int usersNbr)
    {
        this.Filename = filename;
        this.UsersNbr = usersNbr;
    }

    public string Filename
    {
        get;
    }

    public int UsersNbr
    {
        get;
    }
}