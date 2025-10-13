package com.itheima;/*
package com.itheima;

class Outer {
    int m = 0;  					// 定义类的成员变量
    //定义一个成员方法test1()
    void test1() {
        System.out.println("外部类成员方法test1()");
    }
    void test2() {
        //定义一个局部内部类，在局部内部类中访问外部类变量和方法
        class Inner {
            int n = 1;
            void show() {
                System.out.println("外部类成员变量m = " + m);
                test1();
            }
        }
        //访问局部内部类中的变量和方法
        Inner inner = new Inner();
        System.out.println("局部内部类变量n = " + inner.n);
        inner.show();
    }
}
public class Example21 {
    public static void main(String[] args) {
        Outer outer = new Outer();
        outer.test2();     //通过外部类对象outer调用创建了局部内部类的方法test2()
    }
}
*/
