namespace Algorithms.MergeSortedLists
{
    class Solution
    {
        public List<ListNode?> Lists { get; }

        public Solution(List<ListNode?> lists)
        {
            this.Lists = lists;
        }

        public Solution(string filename)
        {
            this.Lists = ListNode.Deserialize(filename);
        }

        public Solution(int k)
        {
            this.Lists = ListNode.GenerateLists(k);
        }

        public ListNode? UseNativeSort()
        {
            return UseNativeSort(Lists);
        }

        public ListNode? UseNativeSort(List<ListNode?> lists)
        {
            var numbers = new List<int>();

            foreach (var list in lists)
            {
                var node = list;
                while (node != null)
                {
                    numbers.Append(node.Value);
                    node = node.Next;
                }
            }

            var head = new ListNode(0);
            var temp = head;
            numbers.Sort();
            foreach (var num in numbers)
            {
                temp = temp.Next = new ListNode(num);
            }

            return head.Next;
        }

        public ListNode? UseBruteForce()
        {
            return UseBruteForce(Lists);
        }

        public ListNode? UseBruteForce(List<ListNode?> lists)
        {
            if (lists.Count == 0)
                return null;

            if (lists.Count == 1)
                return lists[0];

            var left = lists[0];
            for (int i = 1; i < lists.Count; i++)
            {
                left = MergeTwoLists(left, lists[i]);
            } 

            return left;
        }

        public ListNode? UsePriorityQueue()
        {
            return UsePriorityQueue(Lists);
        }

        public ListNode? UsePriorityQueue(List<ListNode?> lists)
        {
            var q = new PriorityQueue<ListNode, int>(lists.Count);

            foreach (var list in lists)
            {
                if (list != null)
                {
                    q.Enqueue(list, list.Value);
                }
            }

            var head = new ListNode(0);
            var node = head;
            while (q.Count > 0)
            {
                var l = q.Dequeue();
                if (l.Next != null)
                {
                    var next = l.Next;
                    q.Enqueue(next, next.Value);
                }
                node = node.Next = new ListNode(l.Value);
            }

            return head.Next;
        }

        public ListNode? DevideAndConquer()
        {
            return DevideAndConquer(Lists);
        }

        public ListNode? DevideAndConquer(List<ListNode?> lists)
        {
            if (lists.Count == 0)
                return null;

            if (lists.Count == 1)
                return lists[0];

            if (lists.Count == 2)
                return MergeTwoLists(lists[0], lists[1]);

            int mdeian = lists.Count / 2;
            var l = lists.Take(mdeian).ToList();
            var left = DevideAndConquer(l);
            var r = lists.Skip(mdeian).ToList();
            var right = DevideAndConquer(r);

            return MergeTwoLists(left, right);
        }

        public ListNode? MergeTwoLists(ListNode? left, ListNode? right)
        {
            ListNode head = new ListNode(0);
            ListNode node = head;
            while (left != null && right != null)
            {
                if (left.Value > right.Value)
                {
                    node.Next = left;
                    left = left.Next;
                }
                else
                {
                    node.Next = right;
                    right = right.Next;
                }

                node = node.Next;
            }

            node.Next = (left != null) ? left : right;
            return head.Next;
        }
    }
}