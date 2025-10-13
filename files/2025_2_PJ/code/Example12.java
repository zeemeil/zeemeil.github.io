package com.itheima;/*
package com.itheima;

//// 定义接口Animal
interface Animal {
    public String NAME = "牧羊犬";       // 定全局常量,名称
    public void shout();                // 定义抽象方法shout()
    public void info();                 // 定义抽象方法info()
}
////定义抽象类Action
abstract class Action {
    public abstract void eat();       // 定义抽象方法eat()
}
//// 定义Dog类继承Action抽象类，并实现Animal接口
class Dog extends Action implements Animal{
    // 实现Action抽象类中的抽象方法eat()
    public void eat() {
        System.out.println("喜欢吃骨头");
    }
    //实现写Animal接口中的抽象方法shout()
    public void shout() {
        System.out.println("汪汪……");
    }
    // 实现Animal接口中的抽象方法info()
    public void info() {
        System.out.println("名称："+NAME);
    }
}
// 定义测试类
class Example12 {
    public static void main(String[] args) {
        Dog dog = new Dog();    		// 创建Dog类的实例对象
        dog.info();               		// 调用Dog类中实现的info()方法
        dog.shout();  		    		// 调用Dog类中实现的shout()方法
        dog.eat();   			    	// 调用Dog类中实现的eat()方法
    }
}
*/
