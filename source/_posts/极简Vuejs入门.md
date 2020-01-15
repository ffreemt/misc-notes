---
title: 极简Vuejs入门
date: 2020-01-13 13:11:15
tags: ['vue', 'vuejs', 'vue.js']
---
## 准备工作
### 引言
本文的vue部分完全基于浏览器和CDN，即是说，无需nodejs环境。

本文并非教程。如果会点node，最好的教程自然是vuejs官方教程。

写本文的初衷是因为在学习vue的过程中，依靠node环境的话往往会陷入各种设置的汪洋之中，而依靠codepen之类的网站又往往有些隔靴搔痒的感觉——写的vue已经工作了，却仍然不知道到底是怎么回事。
本文的特点：没什么废话，每个例子都是极简。真正搞懂了一个例子就了解了一个相关的概念。

### 所需工具
* 浏览器（如Chrome、Firefox等）
* 文本编辑器（如 vscode，notepad++， vim等等）
* 第三个例子开始需要`web/http`服务器
* 最好能学会用浏览器的`devtools`（偶尔交互运行javascript）及安装浏览器扩展 [Vue.js devtools](https://github.com/vuejs/vue-devtools)（用于查看Vue组件的结构）

### 几个极简例子
#### 少于十行码的 vue 网页
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

#### 改进版: 少于十行码的 vue 网页
修改`vue-hello-world.html`进一步分离`html`和`js`, 存为`vue-hello-world1.html`：
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
双击`vue-hello-world1.html`，浏览器显示`hello from vue`

#### 分离成 `html` 和 `js` 文件

`vue-hello.html`:
```html
<div id="app"></div>
<script type="module" src="vue-hello.js"></script>
```

`vue-hello.js`：
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

### `html`及`js`文件样本
前一个例子`vue-hello.js`里用了
```javascript
import Vue from "https://unpkg.com/vue/dist/vue.esm.browser.js";
```

里面的`vue.esm.browser.js`看上去不太和谐。因此我们以后将使用如下的 `html`和`js`：在 `html` 文件里里导入`vue.js`。`hello.html`:
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

启动`http`服务器（例如 `python -m httml.server` 或 `http-server`）。浏览器指向对应的端口及`uri`（例如 `http://127.0.0.1:8000/hello.html` ）后显示 `hello from vue`

以后要用到第三方`js`库也会放在`html`文件里，另外需要用`css`框架(bootstrap, bulma, buefy, element等等)及图标库（Font Awesome，Material Design等）时也会放在`html`文件的头`<head></head>`里。

## `v-bind` 和 `v-model` 绑定
### `v-bind`: 单向绑定
`binding.html`：
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="binding.js"></script>
```

`binding.js`：
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
`<input />`的 `value` 绑定在vue实例`data`的`msg`的值（即`hello from vue`），而且是即时反应的，`msg`变化时，`<input />`的 `value`即时变化。可以打开`devtools`，点击Vue卡（需要先安装浏览器扩展 [Vue.js devtools](https://github.com/vuejs/vue-devtools)）里的Root
![Vue-devtools](/img/vue-root.png)

再在`console`终端卡里输入
```bash
$vm0._data.msg = 'hello again'
```
`<input />`的 `value`即时显示为`hello again`

### `v-model`: 双向绑定
而如果我们在`<input />`框里改变`value`，`Message is:  hello from vue`却不会变化。要达到所谓的双向绑定（改变`<input />`的 `value`时vue实例的`msg`也跟着变化，就需要用到`v-model`。
`editme.html`：
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="editme.js"></script>
```

`editme.js`：
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
## `v-on` 和 `method`
`click-say-hello.html`：
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="click-say-hello.js"></script>
```

`click-say-hello.js`：
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

## `components`: `Vue.component`
### 简单`Component`

`compo1.html`:
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="compo1.js"></script>
```

`compo1.js`:
```javascript
const CompoOne = Vue.component("compo-one", {
  data: function() {
    return { compoMsg: "hello from compo-one" };
  },
  template: "<div>message from compo-one: {{ compoMsg }} </div>"
});

const templ = `
  <div>
    compo-one in #app: <compo-one></compo-one>
  </div>
`;
new Vue({
  el: "#app",
  data() {
    return {
      msg: ""
    };
  },
  components: { CompoOne },
  template: templ
});

```

浏览器指向 `http://127.0.0.1:8080/compo1.html`显示
```txt
compo-one in #app:
message from compo-one: hello from compo-one
```

### `SFC: Single File Component`
将 `compo1.js` 里的 `CompoOne` 分离出来成为单独一个文件就成了所谓的 `Single File Component` 组件。

`app1.html`:
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="app1.js"></script>
```

`app1.js`:
```javascript
import CompoOne from "./CompoOne.js";

const templ = `
  <div>
    compo-one in #app: <compo-one></compo-one>
  </div>
`;
new Vue({
  el: "#app",
  data() {
    return {
      msg: ""
    };
  },
  components: { CompoOne },
  template: templ
});
```

`CompoOne.js`:
```javascript
export default {
  data: function() {
    return { compoMsg: "hello from compo-one" };
  },
  template: "<div>message from compo-one: {{ compoMsg }} </div>"
};
```

浏览器指向 `http://127.0.0.1:8080/app1.html`, 显示和上一个例子的输出相同

```txt
compo-one in #app:
message from compo-one: hello from compo-one
```

#### 题外话：`CompoOne.js` 转 `CompoOne.vue`
只需将 `CompoOne.js` 里的 `template`部分分离出来放在`<template></template>`里，再在其余部分加上 `<script></script>`，就可以转换成nodejs环境下用的组件。

`CompoOne.vue`：
```vue
<template>
  <div>message from compo-one: {{ compoMsg }}</div>
</template>
<script>
export default {
  data: function() {
    return { compoMsg: "hello from compo-one" };
  }
};
</script>
```

例如，在 `nodejs` 环境下运行：
```bash
vue serve CompoOne.vue
```
浏览器指向对应的端口（例如 `http://localhost:8081/`）显示`message from compo-one: hello from compo-one`。


### `props` 组件传参
组件的意义在于可以传入不同的参数多次使用，`props`就是用来传参的。

#### 传固定参数

`app2.html`:
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="app2.js"></script>

```

`app2.js`:
```javascript
import CompoTwo from "./CompoTwo.js";

const templ = `
  <div>
    compo-two name="Alice": <compo-two name="Bob"></compo-two>
    <br/>
    compo-two: name="Bob" <compo-two  name="Alice"></compo-two>
  </div>
`;
new Vue({
  el: "#app",
  data() {
    return {
      msg: ""
    };
  },
  components: { CompoTwo },
  template: templ
});

```

`CompoTwo.js`:
```javascript
export default {
  data: function() {
    return { compoMsg: "hey " + this.name + " hello from compo-two" };
  },
  props: ['name'],
  template: "<div>message from compo-two: {{ compoMsg }} to {{ name }} </div>"
};

```

浏览器指向 `http://127.0.0.1:8080/app2.html`, 显示
```txt
compo-two name="Alice":
message from compo-two: hey Bob hello from compo-two to Bob

compo-two: name="Bob"
message from compo-two: hey Alice hello from compo-two to Alice
```

#### 父组件传参
利用 v-bind 可以传入父组件的数据，从而可以获取用户的输入。

`app3.html`：
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="app3.js"></script>

```

`app3.js`：
```javascript
import CompoThree from "./CompoThree.js";

const templ = `
  <div>
    <input placeholder="Type your name" v-model="msg" />
    <br/>
    <compo-three v-bind:name="msg"></compo-three>
  </div>
`;
new Vue({
  el: "#app",
  data() {
    return {
      msg: ""
    };
  },
  components: { CompoThree },
  template: templ
});

```

`CompoThree.js`：
```javascript
export default {
  props: ['name'],
  template: "<div>Hello {{ name }}! </div>"
};

```

浏览器指向 `http://127.0.0.1:8080/app3.html`，在框里输入 `me`, 浏览器显示
![app3](/img/app3.png)

## `computed` 和 `watch`

前面的组件是在 `template` 里调用 `props`。如想在组件的data里调用则要利用 `vue` 的 `computed` 或 `watch`。例如，下面的做法并不能获取`props`的当前值。

`app-foura.html`:
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="app4a.js"></script>

```

`app-foura.js`:
```javascript
import CompoFoura from "./CompoFoura.js";

const templ = `
  <div>
    <input placeholder="Type your name" v-model="msg" />
    <br/>
    <compo-foura v-bind:name="msg"></compo-foura>
  </div>
`;
new Vue({
  el: "#app",
  data() {
    return {
      msg: ""
    };
  },
  components: { CompoFoura },
  template: templ
});

```

`CompoFoura.js`:
```javascript
export default {
  data: function() {
    return { compoMsg: this.name };
  },
  props: ["name"],
  template: "<div>Hello {{ compoMsg }}! </div>"
};

```
浏览器指向 `http://127.0.0.1:8080/app4a.html`, 但用户输入时，`compoMsg`并无变化：
![app4a](/img/app4a.png)
用户输入 `me` 时，浏览器只显示 `Hello!`，不显示 `Hello me!`。

### 组件 `props` 的使用

`app-four.html`:
```html
<div id="app"></div>

<script src="https://unpkg.com/vue/dist/vue.js"></script>
<script type="module" src="app4.js"></script>

```

`app-four.js`:
```javascript
import CompoFour from "./CompoFour.js";

const templ = `
  <div>
    <input placeholder="Type your name" v-model="msg" />
    <br/>
    <compo-four v-bind:name="msg"></compo-four>
  </div>
`;
new Vue({
  el: "#app",
  data() {
    return {
      msg: ""
    };
  },
  components: { CompoFour },
  template: templ
});


```

`CompoFour.js`:
```javascript
export default {
  data: function() {
    return { compoMsg: this.name };
  },
  props: ["name"],
  watch: {
    name: function(newQuery, oldQuery) {
      this.compoMsg = newQuery
    }
  },
  computed: {
    phraseFromParen: function() {
      return this.name;
    }
  },
  template: "<div>Hello {{ compoMsg }}/{{ phraseFromParen }}! </div>"
};

```
浏览器指向 `http://127.0.0.1:8080/app4.html`, 用户输入 `me` 时，`compoMsg` 和 phraseFromParen 随着变化（显示`Hello me/me!`）：
![app4](/img/app4.png)

## axios


(有时间再继续)