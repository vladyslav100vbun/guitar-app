<template>
	<div>
		<router-link class="btn btn-info" to="/"> Back to Song List</router-link>
		<div v-if="song" class="text-white py-10">
			<h3 class="text-2xl"><span class="text-4xl">{{ song.title }}</span> by {{ song.artist }}</h3>
			<p>Genre: {{ song.genre }}</p>
			<p >Difficulty Level: {{ song.difficulty_level }}</p>
			<p class="text-2xl mt-10">Video</p>
			<iframe
				width="560"
				height="315"
				:src="song.video_link"
				title="YouTube video player"
				allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
				allowfullscreen
			></iframe>
			<p class="text-2xl mt-10">Tabs</p>
			<img class="rounded" :src="song.tablature_photo" alt="">
		</div>
	</div>
</template>

<script>
import axios from "axios";

export default {
	data() {
		return {
			song: null,
		};
	},
	methods: {
		async fetchSongDetail() {
			try {
				const response = await axios.get(`http://localhost:8000/api/songs/${this.$route.params.slug}/`);
				this.song = response.data;
			} catch (error) {
				console.error('Error fetching song detail:', error);
			}
		},
	},
	mounted() {
		this.fetchSongDetail();
	},
};
</script>
