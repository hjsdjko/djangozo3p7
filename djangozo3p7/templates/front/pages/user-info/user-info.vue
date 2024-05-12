<template>
<view class="content">
	<view class="box" :style='{"padding":"0 24rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"24rpx 0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","borderRadius":"0","borderWidth":"0","width":"100%","borderStyle":"solid","height":"auto"}'>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>业主号</view>
			<input disabled="true"  style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(0,0,0,0)","color":"rgba(0, 0, 0, 1)","borderRadius":"16rpx","borderWidth":"2rpx","width":"100%","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' v-model="ruleForm.yezhuhao" placeholder="业主号"></input>
		</view>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>密码</view>
			<input  type="password" style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(0,0,0,0)","color":"rgba(0, 0, 0, 1)","borderRadius":"16rpx","borderWidth":"2rpx","width":"100%","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' v-model="ruleForm.mima" placeholder="密码"></input>
		</view>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>业主姓名</view>
			<input   style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(0,0,0,0)","color":"rgba(0, 0, 0, 1)","borderRadius":"16rpx","borderWidth":"2rpx","width":"100%","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' v-model="ruleForm.yezhuxingming" placeholder="业主姓名"></input>
		</view>
			<view v-if="tableName=='yezhu'" :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' class="cu-form-group select">
                                <view :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}' class="title">性别</view>
                                <picker  @change="yezhuxingbieChange" :value="yezhuxingbieIndex" :range="yezhuxingbieOptions">
                                        <view style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 0px rgba(0,0,0,.6) inset","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"left","borderRadius":"16rpx","borderWidth":"2rpx","width":"calc(100% - 160rpx)","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' class="uni-input picker-select-input">{{ruleForm.xingbie?ruleForm.xingbie:"请选择性别"}}</view>
                                </picker>
                        </view>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>年龄</view>
			<input   style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(0,0,0,0)","color":"rgba(0, 0, 0, 1)","borderRadius":"16rpx","borderWidth":"2rpx","width":"100%","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' v-model="ruleForm.nianling" placeholder="年龄"></input>
		</view>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" @tap="yezhutouxiangTap" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>头像</view>
			<view style="flex: 1;">
				<image :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 auto","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","borderRadius":"100%","borderWidth":"0","width":"88rpx","borderStyle":"solid","height":"88rpx"}' v-if="ruleForm.touxiang" style="margin: 0;" class="avator" :src="baseUrl+ruleForm.touxiang" mode=""></image>
				<image :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 auto","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","borderRadius":"100%","borderWidth":"0","width":"88rpx","borderStyle":"solid","height":"88rpx"}' v-else class="avator" style="margin: 0;" src="../../static/center/face.jpeg" mode=""></image>
			</view>
		</view>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>手机</view>
			<input   style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(0,0,0,0)","color":"rgba(0, 0, 0, 1)","borderRadius":"16rpx","borderWidth":"2rpx","width":"100%","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' v-model="ruleForm.shouji" placeholder="手机"></input>
		</view>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>身份证</view>
			<input   style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(0,0,0,0)","color":"rgba(0, 0, 0, 1)","borderRadius":"16rpx","borderWidth":"2rpx","width":"100%","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' v-model="ruleForm.shenfenzheng" placeholder="身份证"></input>
		</view>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>楼房号</view>
			<input   style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(0,0,0,0)","color":"rgba(0, 0, 0, 1)","borderRadius":"16rpx","borderWidth":"2rpx","width":"100%","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' v-model="ruleForm.loufanghao" placeholder="楼房号"></input>
		</view>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>门牌号</view>
			<input   style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(0,0,0,0)","color":"rgba(0, 0, 0, 1)","borderRadius":"16rpx","borderWidth":"2rpx","width":"100%","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' v-model="ruleForm.menpaihao" placeholder="门牌号"></input>
		</view>
		<view :style='{"padding":"0","boxShadow":"0 0 0px rgba(0,0,0,.3)","margin":"0 0 20rpx 0","borderColor":"rgba(179, 179, 179, 1)","backgroundColor":"rgba(255, 255, 255, 1)","borderRadius":"0","borderWidth":"0 0 0 6rpx","width":"100%","borderStyle":"solid","height":"auto"}' v-if="tableName=='yezhu'" class="cu-form-group">
			<view class="title" :style='{"padding":"0","boxShadow":"0 0 16rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(0,0,0,0)","backgroundColor":"rgba(255, 255, 255, 0)","color":"#333","textAlign":"center","borderRadius":"0","borderWidth":"0","width":"160rpx","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid"}'>地址</view>
			<input   style="padding: 0 30upx" :style='{"padding":"0 20rpx","boxShadow":"0 0 12rpx rgba(0,0,0,0)","margin":"0","borderColor":"rgba(54, 111, 112, 1)","backgroundColor":"rgba(0,0,0,0)","color":"rgba(0, 0, 0, 1)","borderRadius":"16rpx","borderWidth":"2rpx","width":"100%","lineHeight":"88rpx","fontSize":"28rpx","borderStyle":"solid","height":"88rpx"}' v-model="ruleForm.dizhi" placeholder="地址"></input>
		</view>
		
		<view class="btn">
			<button @tap="update()" class="cu-btn lg" :style='{"padding":"0 30rpx","boxShadow":"0 0 16rpx rgba(0,0,0,0) inset","margin":"0 20rpx 0 0","backgroundColor":"rgba(54, 111, 112, 1)","borderColor":"#409EFF","borderRadius":"80rpx","color":"#fff","borderWidth":"0","width":"240rpx","fontSize":"28rpx","borderStyle":"solid","height":"80rpx"}'>保存</button>
			<button @tap="logout()" class="cu-btn lg" :style='{"padding":"0 30rpx","boxShadow":"0 0 16rpx rgba(0,0,0,0) inset","margin":"0","backgroundColor":"rgba(187, 187, 187, 1)","borderColor":"#E6A23C","borderRadius":"80rpx","color":"#fff","borderWidth":"0","width":"200rpx","fontSize":"28rpx","borderStyle":"solid","height":"80rpx"}'>退出登录</button>
		</view>
	</view>
</view>
</template>

<script>
	export default {
		data() {
			return {
				ruleForm: {
				},
				tableName:"",
				yezhuxingbieOptions: [],
				yezhuxingbieIndex: 0,
			}
		},
		computed: {
			baseUrl() {
				return this.$base.url;
			}
		},
		async onLoad() {
			let table = uni.getStorageSync("nowTable");
			let res = await this.$api.session(table);
			this.ruleForm = res.data;
			this.tableName = table;
			// 自定义下拉框值
			if(this.tableName=='yezhu'){
				this.yezhuxingbieOptions = "男,女".split(',');
				this.yezhuxingbieOptions.forEach((item, index) => {
					if(item==this.ruleForm.xingbie) {
						this.yezhuxingbieIndex = index;
					}
				});
			}
			this.styleChange()
		},
		methods: {
                        // 下拉变化
                        yezhuxingbieChange(e) {
                                this.yezhuxingbieIndex = e.target.value
                                this.ruleForm.xingbie = this.yezhuxingbieOptions[this.yezhuxingbieIndex]
                        },
			styleChange() {
				this.$nextTick(()=>{
					// document.querySelectorAll('.cu-form-group .uni-input-input').forEach(el=>{
					//   el.style.backgroundColor = this.userInfoForm.list.input.backgroundColor
					// })
				})
			},
			// 获取uuid
			getUUID () {
				return new Date().getTime();
			},
			logout() {
				uni.setStorageSync('token', '');
				this.$utils.jump('../login/login');
			},
			// 注册
			async update() {
				if((!this.ruleForm.yezhuhao) && `yezhu` == this.tableName){
					this.$utils.msg(`业主号不能为空`);
					return
				}
				if((!this.ruleForm.mima) && `yezhu` == this.tableName){
					this.$utils.msg(`密码不能为空`);
					return
				}
				if(`yezhu` == this.tableName && this.ruleForm.shouji&&(!this.$validate.isMobile(this.ruleForm.shouji))){
					this.$utils.msg(`手机应输入手机格式`);
					return
				}
				if(`yezhu` == this.tableName && this.ruleForm.shenfenzheng&&(!this.$validate.checkIdCard(this.ruleForm.shenfenzheng))){
					this.$utils.msg(`身份证应输入身份证格式`);
					return
				}
				if(`yezhu` == this.tableName && this.ruleForm.money&&(!this.$validate.isNumber(this.ruleForm.money))){
					this.$utils.msg(`余额应输入数字`);
					return
				}
				let table = uni.getStorageSync("nowTable");
				await this.$api.update(table, this.ruleForm);
				this.$utils.msgBack('修改成功');;
			}

			,yezhutouxiangTap() {
				let _this = this;
				this.$api.upload(function(res) {
					_this.ruleForm.touxiang = 'upload/' + res.file;
					_this.$forceUpdate();
				});
			}
		}
	}
</script>

<style lang="scss" scoped>
	page {
		background-color: #fff;
	}
	
	.content:after {
		position: fixed;
		top: 0;
		right: 0;
		left: 0;
		bottom: 0;
		content: '';
				background-attachment: fixed;
		background-size: cover;
		background-position: center;
	}

	.avator {
		width: 110upx;
		height: 110upx;
		border-radius: 50%;
		margin-left: 30upx;
	}
	
	.cu-form-group.active {
		justify-content: space-between;
	}

	.cu-btn {
		width: 100%;
	}
	.cu-form-group .title {
		height: auto;
	}

	.right-input {
		flex: 1;
		text-align: left;
		line-height: 88rpx;
	}
	.btn {
	  display: flex;
	  align-items: center;
	  justify-content: center;
	  flex-wrap: wrap;
	}
	.box {
	  width: auto;
	  padding: 0 10upx;
	  box-sizing: border-box;
	  margin-bottom: 20upx;
	}

.picker-select-input {
	line-height: 88rpx;
}
</style>
