using System.Linq.Expressions;

public class Test<T>
{
    private T soultion;
    public Test(Func<T> ctr) => this.soultion = ctr();
    public Test<T> Mesure(Expression<Action<T>> expr)
    {
        var fn = expr.Compile();
        Utils.Mesure(() =>
        {
            Console.WriteLine(expr.ToString());
            fn(this.soultion);
        });
        return this;
    }
}