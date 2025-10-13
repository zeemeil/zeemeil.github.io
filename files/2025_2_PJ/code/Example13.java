package com.itheima;/*
package com.itheima;

//// 定义接口Animal
interface Animal {
    public String NAME = "牧羊犬";
    public void info();     	// 定义抽象方法info()
}
////定义接口Color
interface Color {
    public void black();       	// 定义抽象方法shout()
}
//定义接口Action，Action同时继承接口Animal和接口Color
interface Action extends Animal,Color{
    public void shout();       	// 定义抽象方法black()
}
//// 定义Dog类实现Action接口
class Dog implements Action{
    // 实现Animal接口中的抽象方法info()
    public void info() {
        System.out.println("名称："+NAME);
    }
    // 实现Color接口中的抽象方法black()
    public void black() {
        System.out.println("黑色");
    }
    // 实现Action接口中的抽象方法shout()
    public void shout() {
        System.out.println("汪汪……");
    }
}
// 定义测试类
class Example13 {
    public static void main(String[] args) {
        Dog dog = new Dog(); 	// 创建Dog类的对象dog
        dog.info();      		// 调用Dog类中实现的info()方法
        dog.shout();     		// 调用Dog类中实现的shout()方法
        dog.black();     		// 调用Dog类中实现的eat()方法
    }
}
*/
