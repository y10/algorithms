using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;

namespace Algorithms.MergeSortedLists
{
    class Solution
    {
        public Func<List<ListNode?>> Generator { get;  }

        public Solution(Func<List<ListNode?>> generator)
        {
            this.Generator = generator;
        }

        public Solution(string filename)
        {
            this.Generator = ()=> ListNode.Deserialize(filename);
        }

        public Solution(int k, int l = 500, int i = 1000)
        {
            this.Generator = () => ListNode.GenerateLists(k);
        }

        public ListNode? UseNativeSort()
        {
            return UseNativeSort(this.Generator());
        }

        public ListNode? UseNativeSort(List<ListNode?> lists)
        {
            var numbers = new List<int>();

            foreach (var list in lists)
            {
                var node = list;
                while (node != null)
                {
                    numbers.Add(node.Value);
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
            return UseBruteForce(this.Generator());
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
            return UsePriorityQueue(this.Generator());
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
                node = node.Next = l;
            }

            return head.Next;
        }

        public ListNode? DivideAndConquer()
        {
            return DivideAndConquerIter(this.Generator());
        }

        public ListNode? DivideAndConquerIter(List<ListNode?> lists)
        {
            int interval = 1;
            while (interval < lists.Count) {
                for (int i = 0; i < lists.Count - interval; interval *= 2)
                {
                    lists[i] = MergeTwoLists(lists[i], lists[i + interval]);
                }
                interval *= 2;
            }

            return lists.Count > 0 ? lists[0] : null;
        }

        public ListNode? DivideAndConquer(IEnumerable<ListNode?> lists)
        {
            int listsCount = lists.Count();
            if (listsCount == 0)
                return null;

            if (listsCount == 1)
                return lists.First();

            int mdeian = listsCount / 2;
            var left = DivideAndConquer(lists.Take(mdeian));
            var right = DivideAndConquer(lists.Skip(mdeian));

            return MergeTwoLists(left, right);
        }

        public ListNode? DivideAndConquer(List<ListNode?> lists, int l, int r)
        {
            if (l > r)
                return null;

            if (l == r)
                return lists[l];

            int mdeian = (r + l) / 2;
            var left = DivideAndConquer(lists, l, mdeian);
            var right = DivideAndConquer(lists, mdeian + 1, r);

            return MergeTwoLists(left, right);
        }

        public ListNode? MergeTwoLists(ListNode? left, ListNode? right)
        {
            ListNode head = new ListNode(0);
            ListNode node = head;
            while (left != null && right != null)
            {
                if (left.Value < right.Value)
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