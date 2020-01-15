---
title: 极简Vuejs入门
date: 2020-01-13 13:11:15
tags: ['vue', 'vuejs', 'vue.js']
---
本文的vue部分完全基于浏览器和CDN，即是说，无需nodejs环境。

本文并非教程。如果会点node，最好的教程自然是vuejs官方教程。

写本文的初衷是因为在学习vue的过程中，依靠node环境的话往往会陷入各种设置的汪洋之中，而依靠codepen之类的网站又往往有些隔靴搔痒的感觉——写的vue已经工作了，却仍然不知道到底是怎么回事。
本文的特点：没什么废话，每个例子都是极简。真正搞懂了一个例子就了解了一个相关的概念。
## 所需工具
* 浏览器
* 文本编辑器（如 vscode，notepad++， vim等等）
* 浏览器扩展 [Vue.js devtools](https://github.com/vuejs/vue-devtools)：用于查看Vue组件的结构
* 第三个例子开始需要`web/http`服务器
* 最好能学会用浏览器的`devtools`及安装`vue-devtools`扩展
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
### 改进版: 少于十行码的 vue 网页
修改`vue-hello-world.html` 文件存为`vue-hello-world1.html`：进一步分离html和js：
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
```Javascript
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

## `html`及`js`文件样本
前一个例子`vue-hello.js`里用了
```javascript
import Vue from "https://unpkg.com/vue/dist/vue.esm.browser.js";
```
里面的`vue.esm.browser.js`看上去不太和谐。因此我们以后将使用如下的 `html`和`js`——在html里导入`vue.js`。`hello.html`:
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="hello.js"></script>
```
`hello.js`:
```javascript
new Vue({
  el: "#app",
  data: { msg: "hello from vue" },
  template: "<div>{{ msg }}</div>"
});
```
启动`http服务器`（例如 `python -m httml.server` 或 `http-server`）。浏览器指向对应的端口及`uri`（例如 `http://127.0.0.1:8000/hello.html` ）后显示 `hello from vue`

以后要用到第三方`js`库也会放在`html`文件里，另外需要用`css`框架库(bootstrap, bulma, buefy, element等等)及图标库（Font Awesome，Material Design等）时也会放在`html`文件的头`<head></head>`里。
## 绑定
### `v-bind`: 单向绑定
`binding.html`
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="binding.js"></script>
```
`binding.js`
```javascript
const templ = `
<div>
<input placeholder="edit me" v-bind:value="msg" />
<p>Message is: {{ msg }}</p>
</div>
`
new Vue({
  el: "#app",
  data: { msg: "hello from vue" },
  template: templ
});
```
`<input />`的 `value` 绑定在vue实例`data`的`msg`的值（即`hello from vue`），而且是即时反应的，`msg`变化时，`<input />`的 `value`即时变化。可以打开`devtools`的`console`终端输入
```bash
vm0._data.msg = 'hello again'
```
`<input />`的 `value`即时显示为`hello again`
### `v-model`: 双向绑定
而如果我们在`<input />`框里改变`value`，`Message is:  hello from vue`却不会变化。要达到所谓的双向绑定（改变`<input />`的 `value`时vue实例的`msg`也跟着变化，就需要用到`v-model`。
`editme.html`
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="editme.js"></script>
```
`editme.js`
```Javascript
const templ = `
<div>
<input placeholder="edit me" v-model="msg" />
<p>Message is: {{ msg }}</p>
</div>
`
new Vue({
  el: "#app",
  data: { msg: "" },
  template: templ
});
```
## `v-on`和`method`
`click-say-hello.html`
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="click-say-hello.js"></script>
```

`click-say-hello.js`
```Javascript
new Vue({
  el: "#app",
  data() {
    return {
      msg: ""
    };
  },
  methods: {
    hello: function(evt) {
      this.msg = "hellooo...";
    }
  },
  template: `
	<div>
		<button v-on:click="hello">Say it</button>
		<p>Saying: {{ msg }}</p>
	</div>
	`
});
```
浏览器指向`http://127.0.0.1:8080/click-say-hello.html`, 点击`Say it` 后浏览器显示：
![click say hello](/img/click-say-hello.png)


(有时间再继续)