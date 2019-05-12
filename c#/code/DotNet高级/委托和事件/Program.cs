using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace 委托和事件
{
    class Program
    {
        delegate void MyDel(string name);
        static void Main(string[] args)
        {
            MyDel mydel = new MyDel(new Program().SayHello);
            mydel("张三");

            Console.WriteLine("Function GetMax");
            object[] objs = { 12, 58, 45, 36, 41, 89, 54, 36, 47 };
            int max = (int)new Program().GetMax(objs, new CompareNum(new Program().CompareInt));
            Console.WriteLine(max);
            Console.ReadKey();
        }
        public void SayHello(string name) {
            Console.WriteLine(name);
        }
        delegate bool CompareNum(object obj1, object obj2);
        private object GetMax(object[] objs,CompareNum compareNum)
        {
            object obj = objs[0];
            for (int i = 1; i < objs.Length; i++)
            {
                if (!compareNum(obj,objs[i]))
                {
                    obj = objs[i];
                }
            }
            return obj;
        }
        public bool CompareInt(object object1,object object2)
        {
            return (int)object1 > (int)object2; 
        }
    }
}
