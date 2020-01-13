---
title: 极简Vuejs入门
date: 2020-01-13 13:11:15
tags: ['vue', 'vuejs', 'vue.js']
---
基于浏览器和CDN，即是说，无需nodejs环境。
## 所需工具
* 浏览器
* 文本编辑器（如 vscode，notepadd++， vim等等）
* 浏览器扩展 [Vue.js devtools](https://github.com/vuejs/vue-devtools)：用于查看Vue组件的结构
* 第三个例子开始需要`web/http`服务器
## 几个极简例子
### 少于十行码的 vue 网页
用文本编辑器生成以下名为 `vue-hello-world.html` 的文件
```html
<div id="app">{{ msg }}</div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script>
  new Vue({
    el: "#app",
    data: { msg: "hello from vue" }
  });
</script>
```
存盘后双击`vue-hello-world.html`，浏览器会显示`hello from vue`
### 少于十行码的 vue 网页改进版
修改`vue-hello-world.html` 文件存为`vue-hello-world1.html`：进一步html和js：
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script>
  new Vue({
    el: "#app",
    data: { msg: "hello from vue" },
    template: "<div>{{ msg }}</div>"
  });
</script>
```
存盘后双击`vue-hello-world1.html`，浏览器会显示`hello from vue`
### `vue-hello-world1.html`分离成`html`和`js`文件
`vue-hello.html`:
```html
<div id="app"></div>
<script type="module" src="vue-hello.js"></script>
```
`vue-hello.js`
```js
import Vue from "https://unpkg.com/vue/dist/vue.esm.browser.js";

new Vue({
  el: "#app",
  data: { msg: "hello from vue" },
  template: "<div>{{ msg }}</div>"
});
```
由于cors问题，点击`vue-hello.html`不能显示结果。需要开一个`http`服务器，例如 `python`下
```bash
python -m http.server
```
或`node`下用`npm install http-server -g`装一个`http`服务器后运行
```
http-server
```
在浏览器地址栏输入相应的端口和文件名，例如
```html
http://127.0.0.1:8000/vue-hello.html
```
浏览器显示`hello from vue`

(有时间再继续)