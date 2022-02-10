namespace Algorithms
{
    class Program
    {
        public static void Main(string[] args)
        {
            Utils.Testit(() => new MostWordyUsers.Solution("./most-wordy-users/list.txt", 3).Run(), (r) =>
                r.Count == 3 &&
                (r["username4"]?.Equals(16) ?? false) &&
                (r["username3"]?.Equals(8) ?? false) &&
                (r["username"]?.Equals(7) ?? false));
        }
    }
}
