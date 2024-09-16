<template>
	<view class="login">
		<view class="content">
			<!-- 头部logo -->
			<view class="logo">
				<image src="../../static/logo.png"></image>
			</view>
			<!-- 主体表单 -->
			<view class="main">
				<u-form labelPosition="left" :model="loginData" :rules="rules" ref="loginForm">
					<u-form-item label="账户" prop="loginData.account" borderBottom>
						<u-input class="form-input" v-model="loginData.account" placeholder="请输入账户" border="none"></u-input>
					</u-form-item>
					<u-form-item label="密码" prop="loginData.password" borderBottom>
						<u-input class="form-input" type="password" v-model="loginData.password" placeholder="请输入密码" border="none"></u-input>
					</u-form-item>
				</u-form>
			</view>
			<!-- 按钮 -->
			<view class="login-button-wrapper">
				<u-button class="login-button" text="登录" @click="startLogin"></u-button>
			</view>
			<!-- 底部信息 -->
			<view class="footer-warp">
				<navigator url="register" open-type="navigate">注册账号</navigator>
			</view>
		</view>
	</view>
</template>

<script>
	import { mapGetter, mapActions } from 'vuex'
	export default {
		data() {
			return {
				loginData: {
					account: '', // 账户
					password: '' // 密码					
				},
				rules: {
					account: {
						type: 'string',
						required: true,
						message: '请输入账户',
						trigger: ['blur', 'change']
					},
					password: {
						type: 'string',
						required: true,
						message: '请输入密码',
						trigger: ['blur', 'change']
					}
				}
			};
		},
		mounted() {
			//this.isLogin();
		},
		methods: {
			...mapActions({
				actionUserLogin: 'login'
			}),
			isLogin() {
				//判断缓存中是否登录过，直接登录
				// try {
				// 	const value = uni.getStorageSync('setUserData');
				// 	if (value) {
				// 		//有登录信息
				// 		console.log("已登录用户：",value);
				// 		_this.$store.dispatch("setUserData",value); //存入状态
				// 		uni.reLaunch({
				// 			url: '../../../pages/index',
				// 		});
				// 	}
				// } catch (e) {
				// 	// error
				// }
			},
			async startLogin(e) {
				const { account, password } = this.loginData
				console.log(account, password )
				if (!account || !password) {
					uni.showToast({
						icon: 'none',
						title: '账户密码不能为空'
					});
					return
				}
				const ret = await this.actionUserLogin({ account, password })
				if(ret.code == 0) {
					uni.showToast({
						icon: 'none',
						title: '登录成功'
					})
					setTimeout(() => {
						uni.switchTab({
							url: '../serve/serve'
						})
					}, 1000)		
				}
			}
		}
	}
</script>

<style>
	/* @import url("../../components/watch-login/css/icon.css"); */
	@import url("./css/main.css");
	.logo {
		box-sizing: border-box;
		width: 120px;
		height: 120px;
		margin: 160px auto 20px;
		image {
			width: 100%;
			height: 100%;
		}
	}
	.footer-warp {
		margin-top: 12px;
		navigator {
			height: 50px;
			line-height: 50px;
			width: 100%;
			text-align: center;
			color: #666;
			font-size: 14px;
		}
	}
</style>
