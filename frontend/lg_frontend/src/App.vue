<template>
	<div class="container mx-auto">
		<Header v-if="isAuth"/>
		<RouterView />
	</div>
</template>

<script>
import Header from "@/components/Header.vue";

export default {
	components: {Header},
	data() {
		return {
			 isAuth: false
		}
	},
	created() {
		this.isAuth = localStorage.getItem('access_token') ? true : false;
		this.$watch(() => localStorage.getItem('access_token'), (newValue) => {
			this.isAuth = newValue ? true : false;
		});
	},
};
</script>


