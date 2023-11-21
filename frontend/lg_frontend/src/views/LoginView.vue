<!-- Login.vue -->
<template>
	<div class="w-full h-screen flex items-center justify-center text-white">
		<div class="max-w-auto p-10 flex flex-col items-center">
			<h2 class="text-4xl mb-4">Login</h2>
			<form class="flex flex-col" @submit.prevent="login">
				<label class="label">
					<span class="label-text text-white">Email:</span>
				</label>
				<input
					type="text"
					placeholder="Enter your email"
					class="input input-ghost w-full max-w-xs"
					v-model="loginData.email" required
				>
				<label class="label">
					<span class="label-text text-white">Password:</span>
				</label>
				<input
					type="password"
					placeholder="Enter your password"
					class="input input-ghost w-full max-w-xs"
					v-model="loginData.password" required
				>
				<button
					class="btn btn-accent btn-active mt-4"
					type="submit"
				>
					Login
				</button>
				<label class="label">
					<span class="label-text-alt text-white">Don't have an account yet?  <router-link to="/signup" class="link">Sign Up</router-link> </span>
				</label>
			</form>
		</div>
	</div>
</template>

<script>
import {getUserInfo, login} from '@/auth.js';

export default {
	data() {
		return {
			loginData: {
				email: '',
				password: '',
			},
		};
	},
	methods: {
		async login() {
			try {
				const response = await login(this.loginData.email, this.loginData.password);
				console.log('Logged in!', response);

				await getUserInfo();

				this.$router.push('/');
			} catch (error) {
				console.error('Login failed!', error);
			}
		},
	},
};
</script>
