package com.itheima;/*
package com.itheima;

//// 定义Animal类
class Animal {
    String name = "牧羊犬";
    // 定义动物叫的方法
    void shout() {
        System.out.println("动物发出叫声");
    }
}
// 定义Dog类继承Animal类
class Dog extends Animal {
    // 重写父类Animal中的shout()方法,扩大了访问权限
    public void shout() {
        super.shout();      // 调用父类中的shout()方法
        System.out.println("汪汪汪……");
    }
    public void printName(){
        System.out.println("名字:"+super.name);      // 访问父类中的name属性
    }
}
// 定义测试类
public class Example05 {
    public static void main(String[] args) {
        Dog dog = new Dog();    // 创建Dog类的对象
        dog.shout();            // 调用Dog类重写的shout()方法
        dog.printName();        // 调用Dog类中的printName()方法
    }
}*/
