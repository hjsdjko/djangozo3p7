(global["webpackJsonp"]=global["webpackJsonp"]||[]).push([["pages/index/index"],{"16c9":function(n,i,e){"use strict";var t=e("9592"),a=e.n(t);a.a},"4afc":function(n,i,e){"use strict";(function(n){Object.defineProperty(i,"__esModule",{value:!0}),i.default=void 0;var t=c(e("a34a")),a=c(e("b94a"));function c(n){return n&&n.__esModule?n:{default:n}}function u(n,i){var e;if("undefined"===typeof Symbol||null==n[Symbol.iterator]){if(Array.isArray(n)||(e=r(n))||i&&n&&"number"===typeof n.length){e&&(n=e);var t=0,a=function(){};return{s:a,n:function(){return t>=n.length?{done:!0}:{done:!1,value:n[t++]}},e:function(n){throw n},f:a}}throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}var c,u=!0,o=!1;return{s:function(){e=n[Symbol.iterator]()},n:function(){var n=e.next();return u=n.done,n},e:function(n){o=!0,c=n},f:function(){try{u||null==e.return||e.return()}finally{if(o)throw c}}}}function r(n,i){if(n){if("string"===typeof n)return o(n,i);var e=Object.prototype.toString.call(n).slice(8,-1);return"Object"===e&&n.constructor&&(e=n.constructor.name),"Map"===e||"Set"===e?Array.from(n):"Arguments"===e||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(e)?o(n,i):void 0}}function o(n,i){(null==i||i>n.length)&&(i=n.length);for(var e=0,t=new Array(i);e<i;e++)t[e]=n[e];return t}function l(n,i,e,t,a,c,u){try{var r=n[c](u),o=r.value}catch(l){return void e(l)}r.done?i(o):Promise.resolve(o).then(t,a)}function s(n){return function(){var i=this,e=arguments;return new Promise((function(t,a){var c=n.apply(i,e);function u(n){l(c,t,a,u,r,"next",n)}function r(n){l(c,t,a,u,r,"throw",n)}u(void 0)}))}}e("94f1");var h=function(){Promise.all([e.e("common/vendor"),e.e("components/uni-ui/lib/uni-icons/uni-icons")]).then(function(){return resolve(e("27be"))}.bind(null,e)).catch(e.oe)},p={components:{uniIcons:h},data:function(){return{rows:2,column:4,iconArr:["cuIcon-same","cuIcon-deliver","cuIcon-evaluate","cuIcon-shop","cuIcon-ticket","cuIcon-cascades","cuIcon-discover","cuIcon-question","cuIcon-pic","cuIcon-filter","cuIcon-footprint","cuIcon-pulldown","cuIcon-pullup","cuIcon-moreandroid","cuIcon-refund","cuIcon-qrcode","cuIcon-remind","cuIcon-profile","cuIcon-home","cuIcon-message","cuIcon-link","cuIcon-lock","cuIcon-unlock","cuIcon-vip","cuIcon-weibo","cuIcon-activity","cuIcon-friendadd","cuIcon-friendfamous","cuIcon-friend","cuIcon-goods","cuIcon-selection"],role:"",menuList:[],swiperMenuList:[],user:{},tableName:"",btnColor:["#409eff","#67c23a","#909399","#e6a23c","#f56c6c","#356c6c","#351c6c","#f093a9","#a7c23a","#104eff","#10441f","#a21233","#503319"],queryList:[{queryName:"商品名称"},{queryName:"车位名称"}],queryIndex:0,searchForm:{shangpinxinxishangpinmingcheng:"",cheweixinxicheweimingcheng:""},CustomBar:"0",autoplaySwiper:!0,intervalSwiper:5e3,swiperList:[],shangpinxinxilist:[],cheweixinxilist:[],homeshangpinxinxilist:[],news:[]}},computed:{baseUrl:function(){return this.$base.url}},onLoad:function(){var i=this;return s(t.default.mark((function e(){var c,u,r;return t.default.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return i.role=n.getStorageSync("role"),c=n.getStorageSync("nowTable"),e.next=4,i.$api.session(c);case 4:u=e.sent,i.user=u.data,i.tableName=c,r=a.default.list(),i.menuList=r,i.menuList.forEach((function(n,e){i.role==n.roleName&&n.frontMenu.forEach((function(n,e){n.child[0].buttons.indexOf("查看")>-1&&i.swiperMenuList.push(n)}))}));case 10:case"end":return e.stop()}}),e)})))()},onShow:function(){var n=this;return s(t.default.mark((function i(){var e,a,c,r,o;return t.default.wrap((function(i){while(1)switch(i.prev=i.next){case 0:return n.btnColor=n.btnColor.sort((function(){return.5-Math.random()})),e=[],i.next=4,n.$api.page("config",{page:1,limit:5});case 4:a=i.sent,c=u(a.data.list);try{for(c.s();!(r=c.n()).done;)o=r.value,o.name.indexOf("picture")>=0&&o.value&&""!=o.value&&null!=o.value&&e.push({img:o.value,title:o.name})}catch(t){c.e(t)}finally{c.f()}return e&&(n.swiperList=e),i.next=10,n.$api.list("news",{page:1,limit:6});case 10:return a=i.sent,n.news=a.data.list,i.next=14,n.$api.recommend("shangpinxinxi",1,6);case 14:return a=i.sent,n.shangpinxinxilist=a.data.list,i.next=18,n.$api.recommend("cheweixinxi",1,6);case 18:return a=i.sent,n.cheweixinxilist=a.data.list,i.next=22,n.$api.list("shangpinxinxi",{page:1,limit:4});case 22:a=i.sent,n.homeshangpinxinxilist=a.data.list;case 24:case"end":return i.stop()}}),i)})))()},methods:{queryChange:function(n){this.queryIndex=n.detail.value,this.searchForm.shangpinxinxishangpinmingcheng="",this.searchForm.cheweixinxicheweimingcheng=""},onSwiperTap:function(n){},onNewsDetailTap:function(n){this.$utils.jump("../news-detail/news-detail?id=".concat(n))},onDetailTap:function(n,i){this.$utils.jump("../".concat(n,"/detail?id=").concat(i))},onPageTap:function(i){0==this.queryIndex&&(n.setStorageSync("indexQueryCondition",this.searchForm.shangpinxinxishangpinmingcheng),this.searchForm.shangpinxinxishangpinmingcheng=""),1==this.queryIndex&&(n.setStorageSync("indexQueryCondition",this.searchForm.cheweixinxicheweimingcheng),this.searchForm.cheweixinxicheweimingcheng=""),n.navigateTo({url:"../".concat(i,"/list"),fail:function(){n.switchTab({url:"../".concat(i,"/list")})}})},onPageTap2:function(i){n.setStorageSync("useridTag",0),n.navigateTo({url:i,fail:function(){n.switchTab({url:i})}})}}};i.default=p}).call(this,e("543d")["default"])},"54eb":function(n,i,e){"use strict";var t;e.d(i,"b",(function(){return a})),e.d(i,"c",(function(){return c})),e.d(i,"a",(function(){return t}));var a=function(){var n=this,i=n.$createElement,e=(n._self._c,n.__map(n.menuList,(function(i,e){var t=n.__get_orig(i),a=n.__map(i.frontMenu,(function(e,t){var a=n.__get_orig(e),c=n.role==i.roleName?n.__map(e.child,(function(i,e){var t=n.__get_orig(i),a=n.__map(i.buttons,(function(e,t){var a=n.__get_orig(e),c="查看"==e&&"yifahuodingdan"!=i.tableName&&"yituikuandingdan"!=i.tableName&&"yiquxiaodingdan"!=i.tableName&&"weizhifudingdan"!=i.tableName&&"yizhifudingdan"!=i.tableName&&"yiwanchengdingdan"!=i.tableName?i.menu.split("列表"):null;return{$orig:a,g0:c}}));return{$orig:t,l0:a}})):null;return{$orig:a,l1:c}}));return{$orig:t,l2:a}}))),t=n.shangpinxinxilist.length>0&&n.shangpinxinxilist[0].tupian?n.shangpinxinxilist[0].tupian.split(","):null,a=n.shangpinxinxilist.length>1&&n.shangpinxinxilist[1].tupian?n.shangpinxinxilist[1].tupian.split(","):null,c=n.shangpinxinxilist.length>2&&n.shangpinxinxilist[2].tupian?n.shangpinxinxilist[2].tupian.split(","):null,u=n.shangpinxinxilist.length>3&&n.shangpinxinxilist[3].tupian?n.shangpinxinxilist[3].tupian.split(","):null,r=n.shangpinxinxilist.length>4&&n.shangpinxinxilist[4].tupian?n.shangpinxinxilist[4].tupian.split(","):null,o=n.shangpinxinxilist.length>5&&n.shangpinxinxilist[5].tupian?n.shangpinxinxilist[5].tupian.split(","):null,l=n.cheweixinxilist.length>0&&n.cheweixinxilist[0].cheweitupian?n.cheweixinxilist[0].cheweitupian.split(","):null,s=n.cheweixinxilist.length>1&&n.cheweixinxilist[1].cheweitupian?n.cheweixinxilist[1].cheweitupian.split(","):null,h=n.cheweixinxilist.length>2&&n.cheweixinxilist[2].cheweitupian?n.cheweixinxilist[2].cheweitupian.split(","):null,p=n.cheweixinxilist.length>3&&n.cheweixinxilist[3].cheweitupian?n.cheweixinxilist[3].cheweitupian.split(","):null,g=n.cheweixinxilist.length>4&&n.cheweixinxilist[4].cheweitupian?n.cheweixinxilist[4].cheweitupian.split(","):null,f=n.cheweixinxilist.length>5&&n.cheweixinxilist[5].cheweitupian?n.cheweixinxilist[5].cheweitupian.split(","):null,x=n.__map(n.news,(function(i,e){var t=n.__get_orig(i),a=i.addtime.split(" ");return{$orig:t,g13:a}})),d=n.__map(n.homeshangpinxinxilist,(function(i,e){var t=n.__get_orig(i),a=i.tupian?i.tupian.split(","):null;return{$orig:t,g14:a}}));n.$mp.data=Object.assign({},{$root:{l3:e,g1:t,g2:a,g3:c,g4:u,g5:r,g6:o,g7:l,g8:s,g9:h,g10:p,g11:g,g12:f,l4:x,l5:d}})},c=[]},"7e7e":function(n,i,e){"use strict";e.r(i);var t=e("4afc"),a=e.n(t);for(var c in t)"default"!==c&&function(n){e.d(i,n,(function(){return t[n]}))}(c);i["default"]=a.a},9592:function(n,i,e){},"9d5b0":function(n,i,e){"use strict";e.r(i);var t=e("54eb"),a=e("7e7e");for(var c in a)"default"!==c&&function(n){e.d(i,n,(function(){return a[n]}))}(c);e("16c9");var u,r=e("f0c5"),o=Object(r["a"])(a["default"],t["b"],t["c"],!1,null,null,null,!1,t["a"],u);i["default"]=o.exports},bd43:function(n,i,e){"use strict";(function(n){e("15dd");t(e("66fd"));var i=t(e("9d5b0"));function t(n){return n&&n.__esModule?n:{default:n}}n(i.default)}).call(this,e("543d")["createPage"])}},[["bd43","common/runtime","common/vendor"]]]);