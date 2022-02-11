class ListNode
{
    public int Value { get; set; }

    public ListNode? Next
    {
        get
        {
            return (NextRef?.TryGetTarget(out ListNode? node) ?? false) ? node : null;
        }
        set
        {
            NextRef = new  WeakReference<ListNode?>(value, trackResurrection: false);
        }
    }

    private WeakReference<ListNode?>? NextRef;

    public ListNode(int value)
    {
        this.Value = value;
    }

    public ListNode(int value, ListNode? next)
    {
        this.Value = value;
        this.Next = next;
    }

    public static ListNode? Create(IEnumerable<int> list)
    {
        ListNode head = new ListNode(0);
        ListNode node = head;
        foreach (var number in list)
        {
            node.Next = new ListNode(number);
            node = node.Next;
        }

        return head.Next;
    }

    public static List<ListNode?> GenerateLists(int k = 1000, int l = 500, int i = 1000)
    {
        var lists = new List<ListNode?>();
        var rnd = new Random();

        for (int a = 0; a < k; a++)
        {
            var list = new List<int>();
            for (int b = 0; b < rnd.Next(0, l); b++)
            {
                list.Add(rnd.Next(i * -1, i));
            }
            list.Sort();
            lists.Add(ListNode.Create(list));
        }
        return lists;
    }

    public int[] ToArray()
    {
        var node = this;
        var list = new List<int>();
        while (node != null)
        {
            list.Add(node.Value);
            node = node.Next;
        }

        return list.ToArray();
    }

    public void Serialize(System.IO.StreamWriter sw)
    {
        var node = this;
        while (node != null)
        {
            sw.Write(node.Value.ToString());
            if (node.Next != null)
            {
                sw.Write(',');
            }
            node = node.Next;
        }
    }

    public static void Serialize(string filename, List<ListNode?> lists)
    {
        using (var fs = File.OpenWrite(filename))
        {
            using (var sw = new StreamWriter(fs))
            {
                foreach (var list in lists)
                {
                    if (list != null)
                    {
                        list.Serialize(sw);
                        sw.WriteLine();
                    }
                }
            }
        }
    }

    public static List<ListNode?> Deserialize(string filename)
    {
        var lists = new List<ListNode?>();

        using (var fs = File.OpenRead(filename))
        {
            using (var sr = new StreamReader(fs))
            {
                var list = ListNode.Deserialize(sr);
                while (list != null)
                {
                    lists.Add(list);
                    list = ListNode.Deserialize(sr);
                }
            }
        }

        return lists;
    }

    public static ListNode? Deserialize(System.IO.StreamReader sr, int maxNodeCount = 10000)
    {
        var line = sr.ReadLine();
        if (line != null)
        {
            var nums = line.Split(',', maxNodeCount);
            var head = new ListNode(int.MinValue);
            var node = head;
            foreach (var num in nums)
            {
                node.Next = new ListNode(int.Parse(num));
                node = node.Next;
            }

            return head.Next;
        }
        return null;
    }
}