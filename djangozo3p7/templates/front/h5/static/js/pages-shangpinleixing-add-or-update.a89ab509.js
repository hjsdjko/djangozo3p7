(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-shangpinleixing-add-or-update"],{"0156":function(e,t,n){"use strict";var r=n("fcb8"),i=n.n(r);i.a},"2c18":function(e,t,n){"use strict";var r=n("4ea4");Object.defineProperty(t,"__esModule",{value:!0}),t.default=void 0,n("a481"),n("c5f6"),n("f559"),n("ac6a"),n("96cf");var i=r(n("3b8d")),a=r(n("e2b1")),o={data:function(){return{cross:"",ruleForm:{shangpinleixing:""},user:{},ro:{shangpinleixing:!1}}},components:{wPicker:a.default},computed:{baseUrl:function(){return this.$base.url}},onLoad:function(){var e=(0,i.default)(regeneratorRuntime.mark((function e(t){var n,r,i,a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return n=uni.getStorageSync("nowTable"),e.next=3,this.$api.session(n);case 3:if(r=e.sent,this.user=r.data,this.ruleForm.userid=uni.getStorageSync("userid"),t.refid&&(this.ruleForm.refid=t.refid,this.ruleForm.nickname=uni.getStorageSync("nickname")),!t.id){e.next=13;break}return this.ruleForm.id=t.id,e.next=11,this.$api.info("shangpinleixing",this.ruleForm.id);case 11:r=e.sent,this.ruleForm=r.data;case 13:if(this.cross=t.cross,!t.cross){e.next=25;break}i=uni.getStorageSync("crossObj"),e.t0=regeneratorRuntime.keys(i);case 17:if((e.t1=e.t0()).done){e.next=25;break}if(a=e.t1.value,"shangpinleixing"!=a){e.next=23;break}return this.ruleForm.shangpinleixing=i[a],this.ro.shangpinleixing=!0,e.abrupt("continue",17);case 23:e.next=17;break;case 25:this.styleChange();case 26:case"end":return e.stop()}}),e,this)})));function t(t){return e.apply(this,arguments)}return t}(),methods:{styleChange:function(){this.$nextTick((function(){}))},getUUID:function(){return(new Date).getTime()},onSubmitTap:function(){var e=(0,i.default)(regeneratorRuntime.mark((function e(){var t,n,r,i,a,o,s,u,c,d;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(this.ruleForm.shangpinleixing){e.next=3;break}return this.$utils.msg("商品类型不能为空"),e.abrupt("return");case 3:if(!this.cross){e.next=19;break}if(i=uni.getStorageSync("statusColumnName"),a=uni.getStorageSync("statusColumnValue"),""==i){e.next=19;break}if(o=uni.getStorageSync("crossObj"),i.startsWith("[")){e.next=15;break}for(s in o)s==i&&(o[s]=a);return u=uni.getStorageSync("crossTable"),e.next=13,this.$api.update("".concat(u),o);case 13:e.next=19;break;case 15:t=Number(uni.getStorageSync("userid")),n=o["id"],r=uni.getStorageSync("statusColumnName"),r=r.replace(/\[/,"").replace(/\]/,"");case 19:if(!n||!t){e.next=41;break}return this.ruleForm.crossuserid=t,this.ruleForm.crossrefid=n,c={page:1,limit:10,crossuserid:t,crossrefid:n},e.next=25,this.$api.list("shangpinleixing",c);case 25:if(d=e.sent,!(d.data.total>=r)){e.next=31;break}return this.$utils.msg(uni.getStorageSync("tips")),e.abrupt("return",!1);case 31:if(!this.ruleForm.id){e.next=36;break}return e.next=34,this.$api.update("shangpinleixing",this.ruleForm);case 34:e.next=38;break;case 36:return e.next=38,this.$api.add("shangpinleixing",this.ruleForm);case 38:this.$utils.msgBack("提交成功");case 39:e.next=49;break;case 41:if(!this.ruleForm.id){e.next=46;break}return e.next=44,this.$api.update("shangpinleixing",this.ruleForm);case 44:e.next=48;break;case 46:return e.next=48,this.$api.add("shangpinleixing",this.ruleForm);case 48:this.$utils.msgBack("提交成功");case 49:case"end":return e.stop()}}),e,this)})));function t(){return e.apply(this,arguments)}return t}(),optionsChange:function(e){this.index=e.target.value},bindDateChange:function(e){this.date=e.target.value},getDate:function(e){var t=new Date,n=t.getFullYear(),r=t.getMonth()+1,i=t.getDate();return"start"===e?n-=60:"end"===e&&(n+=2),r=r>9?r:"0"+r,i=i>9?i:"0"+i,"".concat(n,"-").concat(r,"-").concat(i)},toggleTab:function(e){this.$refs[e].show()}}};t.default=o},a933:function(e,t,n){"use strict";n.r(t);var r=n("2c18"),i=n.n(r);for(var a in r)"default"!==a&&function(e){n.d(t,e,(function(){return r[e]}))}(a);t["default"]=i.a},b080:function(e,t,n){var r=n("24fb");t=r(!1),t.push([e.i,'@charset "UTF-8";\n/**\r\n * 这里是uni-app内置的常用样式变量\r\n *\r\n * uni-app 官方扩展插件及插件市场（https://ext.dcloud.net.cn）上很多三方插件均使用了这些样式变量\r\n * 如果你是插件开发者，建议你使用scss预处理，并在插件代码中直接使用这些变量（无需 import 这个文件），方便用户通过搭积木的方式开发整体风格一致的App\r\n *\r\n */\n/**\r\n * 如果你是App开发者（插件使用者），你可以通过修改这些变量来定制自己的插件主题，实现自定义主题功能\r\n *\r\n * 如果你的项目同样使用了scss预处理，你也可以直接在你的 scss 代码中使用如下变量，同时无需 import 这个文件\r\n */\n/* 颜色变量 */\n/* 行为相关颜色 */\n/* 文字基本颜色 */\n/* 背景颜色 */\n/* 边框颜色 */\n/* 尺寸变量 */\n/* 文字尺寸 */\n/* 图片尺寸 */\n/* Border Radius */\n/* 水平间距 */\n/* 垂直间距 */\n/* 透明度 */\n/* 文章场景相关 */.container[data-v-49f48ef2]{padding:%?20?%}.content[data-v-49f48ef2]:after{position:fixed;top:0;right:0;left:0;bottom:0;content:"";background-attachment:fixed;background-size:cover;background-position:50%}uni-textarea[data-v-49f48ef2]{border:%?1?% solid #eee;border-radius:%?20?%;padding:%?20?%}.title[data-v-49f48ef2]{width:%?180?%}.avator[data-v-49f48ef2]{width:%?150?%;height:%?60?%}.right-input[data-v-49f48ef2]{-webkit-box-flex:1;-webkit-flex:1;flex:1;text-align:left;padding:0 %?24?%}.cu-form-group.active[data-v-49f48ef2]{-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between}.btn[data-v-49f48ef2]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-flex-wrap:wrap;flex-wrap:wrap;padding:%?20?% 0}.cu-form-group[data-v-49f48ef2]{padding:0 %?24?%;background-color:initial;min-height:inherit}.cu-form-group + .cu-form-group[data-v-49f48ef2]{border:0}.cu-form-group uni-input[data-v-49f48ef2]{padding:0 %?30?%}.uni-input[data-v-49f48ef2]{padding:0 %?30?%}.cu-form-group uni-textarea[data-v-49f48ef2]{padding:%?30?%;margin:0}.cu-form-group uni-picker[data-v-49f48ef2]::after{line-height:%?80?%}.select .uni-input[data-v-49f48ef2]{line-height:%?80?%}.input .right-input[data-v-49f48ef2]{line-height:%?88?%}',""]),e.exports=t},c1ff:function(e,t,n){"use strict";n.r(t);var r=n("c740"),i=n("a933");for(var a in i)"default"!==a&&function(e){n.d(t,e,(function(){return i[e]}))}(a);n("0156");var o,s=n("f0c5"),u=Object(s["a"])(i["default"],r["b"],r["c"],!1,null,"49f48ef2",null,!1,r["a"],o);t["default"]=u.exports},c740:function(e,t,n){"use strict";var r,i=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("v-uni-view",{staticClass:"content"},[n("v-uni-form",{staticClass:"app-update-pv"},[n("v-uni-view",{staticClass:"cu-form-group",style:{padding:"0",boxShadow:"0 0 0px rgba(0,0,0,.3)",margin:"0 0 20rpx 0",borderColor:"#ccc",backgroundColor:"rgba(255, 255, 255, 1)",borderRadius:"0",borderWidth:"0",width:"100%",borderStyle:"solid",height:"108rpx"}},[n("v-uni-view",{staticClass:"title",style:{padding:"0",boxShadow:"0 0 16rpx rgba(0,0,0,0)",margin:"0",borderColor:"#ccc",backgroundColor:"rgba(0,0,0,0)",color:"rgba(0, 0, 0, 1)",textAlign:"center",borderRadius:"0",borderWidth:"0",width:"160rpx",lineHeight:"80rpx",fontSize:"28rpx",borderStyle:"solid"}},[e._v("商品类型")]),n("v-uni-input",{style:{padding:"0 30rpx",boxShadow:"0 0 0px rgba(0,0,0,.6) inset",margin:"0",borderColor:"rgba(54, 111, 112, 1)",backgroundColor:"rgba(255, 255, 255, 0)",color:"rgba(0, 0, 0, 1)",textAlign:"left",borderRadius:"16rpx",borderWidth:"2rpx",width:"calc(100% - 160rpx)",fontSize:"28rpx",borderStyle:"solid",height:"88rpx"},attrs:{disabled:e.ro.shangpinleixing,placeholder:"商品类型"},model:{value:e.ruleForm.shangpinleixing,callback:function(t){e.$set(e.ruleForm,"shangpinleixing",t)},expression:"ruleForm.shangpinleixing"}})],1),n("v-uni-view",{staticClass:"btn"},[n("v-uni-button",{staticClass:"bg-red",style:{padding:"0",boxShadow:"0 0 0px rgba(0,0,0,0) inset",margin:"20rpx 0 0 ",backgroundColor:"rgba(54, 111, 112, 1)",borderColor:"#409EFF",borderRadius:"80rpx",color:"#fff",borderWidth:"0",width:"60%",fontSize:"28rpx",borderStyle:"solid",height:"80rpx"},on:{click:function(t){arguments[0]=t=e.$handleEvent(t),e.onSubmitTap.apply(void 0,arguments)}}},[e._v("提交")])],1)],1)],1)},a=[];n.d(t,"b",(function(){return i})),n.d(t,"c",(function(){return a})),n.d(t,"a",(function(){return r}))},fcb8:function(e,t,n){var r=n("b080");"string"===typeof r&&(r=[[e.i,r,""]]),r.locals&&(e.exports=r.locals);var i=n("4f06").default;i("0fd489b8",r,!0,{sourceMap:!1,shadowMode:!1})}}]);