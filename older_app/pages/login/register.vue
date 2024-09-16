<template>
	<view class="register">
		<view class="content">
			<!-- 头部logo -->
			<view class="logo">
				<image src="../../static/logo.png"></image>
			</view>
			<!-- 主体表单 -->
			<view class="main">
				<u-form labelPosition="left" :model="loginData" :rules="rules" ref="loginForm">
					<u-form-item label="姓名" prop="loginData.name" borderBottom>
						<u-input class="form-input" v-model="loginData.name" placeholder="请输入姓名" border="none"></u-input>
					</u-form-item>
					<u-form-item label="账户" prop="loginData.account" borderBottom>
						<u-input class="form-input" v-model="loginData.account" placeholder="请输入账户" border="none"></u-input>
					</u-form-item>
					<u-form-item label="密码" prop="loginData.password" borderBottom>
						<u-input class="form-input" type="password" v-model="loginData.password" placeholder="请输入密码" border="none"></u-input>
					</u-form-item>
					<u-form-item label="性别" prop="loginData.sex" borderBottom>
						<u-picker :show="sexPickerShow" :columns="sexPickerOptions" @cancel="onCloseSexPicker" @confirm="onSelectSex" title="性别" :closeOnClickOverlay="true"></u-picker>
						<u-button class="picker-btn" @click="sexPickerShow = true">{{ sexPickerOptions[0][loginData.sex] }}</u-button>
					</u-form-item>
					<u-form-item label="生日" prop="loginData.birthDate" borderBottom>
						<u-datetime-picker :show="birthPickerShow" v-model="loginData.birthDateTimestamp" :minDate="birthMin" :maxDate="birthMax" mode="date" :formatter="dateFormatter" @confirm="onSelectBirth" @cancel="onCloseBirthPicker"></u-datetime-picker>
						<u-button class="picker-btn" @click="birthPickerShow = true">{{ loginData.birthDate || '请选择出生年月日' }}</u-button>
					</u-form-item>
				</u-form>
			</view>
			<!-- 按钮 -->
			<view class="login-button-wrapper">
				<u-button class="login-button" text="注册" @click="startReg"></u-button>
			</view>
		</view>
	</view>
</template>

<script>
	import { mapGetter, mapActions } from 'vuex'
	import { formatDate } from '../../utils/utils.js'
	export default {
		data() {
			return {
				loading: false,
				// 性别选择器
				sexPickerShow: false,
				sexPickerOptions: [[ '男', '女' ]],
				// 生日选择器
				birthPickerShow: false,
				birthMin: Number(new Date("1930-01-01")),
				birthMax: Number(new Date()),
				loginData: {
					name: '', // 姓名
					account: '', // 账户
					password: '', // 密码
					sex: 0, // 性别
					birthDateTimestamp: Number(new Date()), // 出生时间戳
					birthDate: '', // 出生年月日
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
			}
		},
		mounted() {

		},
		methods: {
			...mapActions({
				actionUserRegister: 'register'
			}),
			// 选择性别
			onSelectSex(e) {
				console.log(e)
				this.loginData.sex = e.indexs[0]
				this.onCloseSexPicker()
			},
			onCloseSexPicker() {
				this.sexPickerShow = false
			},
			// 选择生日
			onSelectBirth(e) {
				console.log(e)
				const { value } = e
				this.loginData.birthDate = formatDate(new Date(value))
				this.onCloseBirthPicker()
			},
			onCloseBirthPicker() {
				this.birthPickerShow = false
			},
			dateFormatter(type, value) {
				if (type === 'year') {
					return `${value}年`
				}
				if (type === 'month') {
					return `${value}月`
				}
				if (type === 'day') {
					return `${value}日`
				}
				return value
			},
			async startReg() {
				//注册
				if (this.loading) {
					//判断是否加载中，避免重复点击请求
					return false;
				}
				const { name, account, password, sex, birthDateTimestamp, birthDate } = this.loginData
				if (!name || !account || !password || !birthDate) {
					uni.showToast({
						icon: 'none',
						title: '信息不完整'
					});
					return
				}
				this.loading = true
				const ret = await this.actionUserRegister({ name, account, password, sex, birthDateTimestamp, birthDate })
				if(ret.code == 0) {
					uni.showToast({
						icon: 'none',
						title: '注册成功'
					})
					setTimeout(() => {
						uni.navigateTo({
							url: './login'
						})
					}, 2000)
				} else {
					this.loading = false
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
</style>
