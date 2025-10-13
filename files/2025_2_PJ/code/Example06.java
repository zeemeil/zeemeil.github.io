package com.itheima;/*
package com.itheima;

//// 定义Animal类
class Animal {
    private String name;
    private int age;
    public Animal(String name, int age) {	// Animal类有参构造方法
        this.name = name;
        this.age = age;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }
    public void setAge(int age) {
        this.age = age;
    }
    public String info() {
        return "名称："+this.getName()+",年龄："+this.getAge();
    }
}
//// 定义Dog类继承Animal类
class Dog extends Animal {
    private String color;
    public Dog(String name, int age, String color) {
        super(name, age);    //通过super关键字调用Animal类有两个参数的构造方法
        this.setColor(color);
    }
    public String getColor() {
        return color;
    }
    public void setColor(String color) {
        this.color = color;
    }
    // 重写父类的info()方法
    public String info() {
        return super.info()+",颜色："+this.getColor();  // 扩充父类中的方法
    }
}
// 定义测试类
public class Example06 {
    public static void main(String[] args) {
        Dog dog = new Dog("牧羊犬",3,"黑色");             // 创建Dog类的对象
        System.out.println(dog.info());
    }
}
*/
