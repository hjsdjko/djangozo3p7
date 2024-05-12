import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
    import news from '@/views/modules/news/list'
    import yezhu from '@/views/modules/yezhu/list'
    import discusscheweixinxi from '@/views/modules/discusscheweixinxi/list'
    import shangpinxinxi from '@/views/modules/shangpinxinxi/list'
    import storeup from '@/views/modules/storeup/list'
    import users from '@/views/modules/users/list'
    import yudingchewei from '@/views/modules/yudingchewei/list'
    import cheweixinxi from '@/views/modules/cheweixinxi/list'
    import tingchefeiyong from '@/views/modules/tingchefeiyong/list'
    import jiaofeixinxi from '@/views/modules/jiaofeixinxi/list'
    import chuchangxinxi from '@/views/modules/chuchangxinxi/list'
    import chat from '@/views/modules/chat/list'
    import discussshangpinxinxi from '@/views/modules/discussshangpinxinxi/list'
    import ruchangxinxi from '@/views/modules/ruchangxinxi/list'
    import messages from '@/views/modules/messages/list'
    import orders from '@/views/modules/orders/list'
    import shangpinleixing from '@/views/modules/shangpinleixing/list'
    import config from '@/views/modules/config/list'


//2.配置路由   注意：名字
const routes = [{
    path: '/index',
    name: '首页',
    component: Index,
    children: [{
      // 这里不设置值，是把main作为默认页面
      path: '/',
      name: '首页',
      component: Home,
      meta: {icon:'', title:'center'}
    }, {
      path: '/updatePassword',
      name: '修改密码',
      component: UpdatePassword,
      meta: {icon:'', title:'updatePassword'}
    }, {
      path: '/pay',
      name: '支付',
      component: pay,
      meta: {icon:'', title:'pay'}
    }, {
      path: '/center',
      name: '个人信息',
      component: center,
      meta: {icon:'', title:'center'}
    }
      ,{
	path: '/news',
        name: '社区资讯',
        component: news
      }
      ,{
	path: '/yezhu',
        name: '业主',
        component: yezhu
      }
      ,{
	path: '/discusscheweixinxi',
        name: '车位信息评论',
        component: discusscheweixinxi
      }
      ,{
	path: '/shangpinxinxi',
        name: '商品信息',
        component: shangpinxinxi
      }
      ,{
	path: '/storeup',
        name: '我的收藏管理',
        component: storeup
      }
      ,{
	path: '/users',
        name: '管理员',
        component: users
      }
      ,{
	path: '/yudingchewei',
        name: '预定车位',
        component: yudingchewei
      }
      ,{
	path: '/cheweixinxi',
        name: '车位信息',
        component: cheweixinxi
      }
      ,{
	path: '/tingchefeiyong',
        name: '停车费用',
        component: tingchefeiyong
      }
      ,{
	path: '/jiaofeixinxi',
        name: '缴费信息',
        component: jiaofeixinxi
      }
      ,{
	path: '/chuchangxinxi',
        name: '出场信息',
        component: chuchangxinxi
      }
      ,{
	path: '/chat',
        name: '在线咨询',
        component: chat
      }
      ,{
	path: '/discussshangpinxinxi',
        name: '商品信息评论',
        component: discussshangpinxinxi
      }
      ,{
	path: '/ruchangxinxi',
        name: '入场信息',
        component: ruchangxinxi
      }
      ,{
	path: '/messages',
        name: '投诉意见',
        component: messages
      }
      ,{
        path: '/orders/:status',
        name: '订单管理',
        component: orders
      }
      ,{
	path: '/shangpinleixing',
        name: '商品类型',
        component: shangpinleixing
      }
      ,{
	path: '/config',
        name: '轮播图管理',
        component: config
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {icon:'', title:'login'}
  },
  {
    path: '/register',
    name: 'register',
    component: register,
    meta: {icon:'', title:'register'}
  },
  {
    path: '/',
    name: '首页',
    redirect: '/index'
  }, /*默认跳转路由*/
  {
    path: '*',
    component: NotFound
  }
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
  mode: 'hash',
  /*hash模式改为history*/
  routes // （缩写）相当于 routes: routes
})

export default router;
