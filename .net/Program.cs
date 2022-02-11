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

        public static void TestMergeSortedListsByDivideAndConquer()
        {
            Utils.Assert(() => new MergeSortedLists.Solution(new List<ListNode?>{
                    ListNode.Create(new int[] {1,2,3,4,5}),
                    ListNode.Create(new int[] {4,5,6,7,8}),
                    ListNode.Create(new int[] {11,12,13,14,15})
            }).DivideAndConquer(), r =>
            {
                var line = string.Join(',', r?.ToArray()?.Select(x => x.ToString()) ?? Enumerable.Empty<string>());
                Console.Write(line);
                Console.WriteLine();
                return line == "1,2,3,4,4,5,5,6,7,8,11,12,13,14,15";
            });
        }

        public static void MesureMergeSortedLists()
        {
            Utils.Testit(() => new MergeSortedLists.Solution(new List<ListNode?>{
                    ListNode.Create(new int[] {1,2,3,4,5}),
                    ListNode.Create(new int[] {4,5,6,7,8}),
                    ListNode.Create(new int[] {11,12,13,14,15})
             }))
             .Mesure((test) => test.UseNativeSort())
             .Mesure((test) => test.UseBruteForce())
             .Mesure((test) => test.DivideAndConquer())
             .Mesure((test) => test.UsePriorityQueue());
        }

        public static void MesureGenMergeSortedLists()
        {
            Utils.Testit(() => new MergeSortedLists.Solution(100000))
            //.Mesure((test) => test.UseNativeSort())
            //.Mesure((test) => test.UseBruteForce());
            //.Mesure((test) => test.UsePriorityQueue());
            .Mesure((test) => test.DivideAndConquer());
        }

        public static void MesureBigMergeSortedLists()
        {
            Utils.Testit(() => new MergeSortedLists.Solution(filename: "./merge-sorted-lists/lists.txt"))
            //.Mesure((test) => test.UseNativeSort())
            //.Mesure((test) => test.UseBruteForce());
            //.Mesure((test) => test.UsePriorityQueue());
            .Mesure((test) => test.DivideAndConquer());
        }

        public static void Main(string[] args)
        {
            TestMergeSortedListsByDivideAndConquer();
        }
    }
}
