<!-- Signup.vue -->
<template>
	<div class="w-full h-screen flex items-center justify-center text-white">
		<div class="max-w-auto p-10 flex flex-col items-center">
			<h2 class="text-4xl mb-4">Signup</h2>
			<form class="flex flex-col" @submit.prevent="signup">
				<label class="label">
					<span class="label-text text-white">First Name:</span>
				</label>
				<input
					type="text"
					placeholder="Enter your first name"
					class="input input-ghost w-full max-w-xs"
					v-model="signupData.first_name" required
				>
				<label class="label">
					<span class="label-text text-white">Last Name:</span>
				</label>
				<input
					type="text"
					placeholder="Enter your last name"
					class="input input-ghost w-full max-w-xs"
					v-model="signupData.last_name" required
				>
				<label class="label">
					<span class="label-text text-white">Email:</span>
				</label>
				<input
					type="email"
					placeholder="Enter your email"
					class="input input-ghost w-full max-w-xs"
					v-model="signupData.email" required
				>
				<label class="label">
					<span class="label-text text-white">Password:</span>
				</label>
				<input
					type="password"
					placeholder="Enter your password"
					class="input input-ghost w-full max-w-xs"
					v-model="signupData.password" required
				>
				<label class="label">
					<span class="label-text text-white">Do you want to teach or study?</span>
				</label>
				<select v-model="signupData.user_type" class="select select-ghost w-full max-w-xs">
					<option disabled selected>Choose role</option>
					<option value="teacher">Teacher</option>
					<option value="student">Student</option>
				</select>

				<label class="label">
					<span class="label-text text-white">Choose avatar:</span>
				</label>
				<input
					type="file"
					class="file-input file-input-ghost w-full max-w-xs"
					@change="handleFileUpload"
				>
				<button
					class="btn btn-accent btn-active mt-4"
					type="submit"
				>
					Signup
				</button>
				<label class="label">
					<span class="label-text-alt text-white">Already have an account?  <router-link to="/" class="link">Log In</router-link> </span>
				</label>
			</form>
		</div>
	</div>
</template>

<script>
import api from '@/api.js';
export default {
	data() {
		return {
			signupData: {
				first_name: '',
				last_name: '',
				email: '',
				password: '',
				confirmPassword: '',
				user_type: 'student',
				avatar: null,
			},
		};
	},
	methods: {
		async signup() {
			try {
				const formData = new FormData();
				for (const key in this.signupData) {
					formData.append(key, this.signupData[key]);
				}
				const response = await api.post('register/', formData, {
					headers: {
						'Content-Type': 'multipart/form-data'
					},
				});
				this.signupData.first_name = ''
				this.signupData.last_name = ''
				this.signupData.email = ''
				this.signupData.password = ''
				this.signupData.confirmPassword = ''
				this.signupData.user_type = 'student'
				this.signupData.avatar = null
				console.log('Signed up!', response.data);
			} catch (error) {
				console.error('Signup failed!', error);
			}
		},
		handleFileUpload(event) {
			const file = event.target.files[0];
			this.signupData.avatar = file;
		},
	},
};
</script>
