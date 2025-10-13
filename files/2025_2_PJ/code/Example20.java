package com.itheima;/*
package com.itheima;

class Outer {
    int m = 0; 						// 定义类的成员变量
    //外部类方法test1()
    void test1() {
        System.out.println("外部类成员方法test1()");
    }
    // 下面的代码定义了一个成员内部类Inner
    class Inner {
        int n = 1;
        void show1() {
            // 在成员内部类的方法中访问外部类的成员变量m
            System.out.println("外部成员变量m = " + m);
            // 在成员内部类的方法中访问外部类的成员方法test1()
            test1();
        }
        void show2() {
            System.out.println("内部成员方法show2()");
        }
    }
    //外部类方法test2()
    void test2() {
        Inner inner = new Inner();		                 //实例化内部类对象inner
        System.out.println("内部成员变量n = " + inner.n); //访问内部类变量和方法
        inner.show2();
    }
}
public class Example20 {
    public static void main(String[] args) {
        Outer outer = new Outer();				//实例化外部类对象outer
        Outer.Inner inner = outer.new Inner();	//实例化内部类对象inner
        inner.show1();		 //在内部类中访问外部类的成员变量m和成员方法test1()
        outer.test2();		 //在内部类中访问内部类的成员变量n和成员方法show2()
    }
}
*/
