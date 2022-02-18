package classes;
public class Item implements java.lang.Comparable<Item> {
    public int priority;
    public int value;
    
    public Item(int p, int v) {
        priority = p;
        value = v;
    }
    
    @Override
    public int compareTo(Item i) {
        return i.priority - this.priority;
    }
}
