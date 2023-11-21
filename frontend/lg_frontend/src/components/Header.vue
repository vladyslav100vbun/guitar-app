<template>
	<div v-if="userData.user_type != ''" class="navbar p-5">
		<div class="flex-1">
			<a class="logo text-2xl text-white">Learn Guitar</a>
		</div>
		<div class="flex-none gap-2 flex items-start text-white">
			<div class="left flex flex-col items-end mr-4">
				<div class="name">Hi, {{ userData.first_name }} {{userData.last_name}}</div>
				<a class="link" @click="performLogout">Logout</a>
			</div>
			<div class="avatar">
				<div class="w-14 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
					<img :src="imgUrl+userData.avatar"/>
				</div>
			</div>
		</div>
	</div>
</template>
<script>


import {axiosInstance} from "@/auth";

export default {
	data() {
		return {
			userData: JSON.parse(localStorage.getItem('user_info')),
			imgUrl: `http://127.0.0.1:8000`
		}
	},
	methods: {
		async performLogout() {
			try {
				localStorage.removeItem('access_token');
				localStorage.removeItem('refresh_token');
				localStorage.removeItem('user_info')
				delete axiosInstance.defaults.headers.common['Authorization'];
				console.log('Logout successful');
				this.$router.push('/login')
			} catch (error) {
				console.error('Logout failed', error.message);
			}
		}
	}
}
</script>

