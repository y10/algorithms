namespace Algorithms
{
    class Program
    {
        public static void TestMostWordyUsers()
        {
            Utils.Assert(() => new MostWordyUsers.Solution("./most-wordy-users/list.txt", 3).Run(), (r) =>
               r.Count == 3 &&
               (r["username4"]?.Equals(16) ?? false) &&
               (r["username3"]?.Equals(8) ?? false) &&
               (r["username"]?.Equals(7) ?? false));
        }

        public static void TestMergeSortedLists()
        {
            Utils.Testit(() => new MergeSortedLists.Solution(filename: "./merge-sorted-lists/lists.txt"))
                 .Mesure((test) => test.UseNativeSort())
                 //.Mesure((test) => test.UseBruteForce())
                 .Mesure((test) => test.UsePriorityQueue());
                 //.Mesure((test) => test.DevideAndConquer());
        }

        public static void Main(string[] args)
        {
            TestMergeSortedLists();
        }
    }
}
