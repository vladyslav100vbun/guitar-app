<template>
	<div>
		<div class="flex">

				<select v-model="alphabeticalOrder" @change="filterSongs" class="select w-full max-w-xs flex-1 mx-2">
					<option value="asc">Ascending</option>
					<option value="desc">Descending</option>
				</select>
				<select v-model="genreFilter" @change="filterSongs" class="select w-full max-w-xs flex-1 mx-2">
					<option value="">All Genres</option>
					<option v-for="genre in genres" :key="genre" :value="genre">{{ genre }}</option>
				</select>


				<select v-model="difficultyFilter" @change="filterSongs" class="select w-full max-w-xs flex-1 mx-2">
					<option value="">All Levels</option>
					<option v-for="level in difficultyLevels" :key="level" :value="level">{{ level }}</option>
				</select>

				<input class="input w-full max-w-xs flex-4 mx-2" type="text" v-model="searchQuery" @input="filterSongs" placeholder="Search..." />
				<button v-if="userData.user_type === 'teacher'" class="btn btn-success mx-2" @click="toggleAddModal">+ Add new song</button>
		</div>

		<div v-if="isAddModalOpen" class="">
				<form @submit.prevent="addSong" method="dialog" class="p-10 text-white">
					<h2 class="text-xl">Add New Song</h2>
					<div>
						<div class="flex justify-between">
							<div>
								<label class="label">
									<span class="label-text text-white">Title</span>
								</label>
								<input
									type="text"
									placeholder="Enter song title"
									class="input w-full max-w-xs"
									v-model="newSong.title" required
								>

								<label class="label">
									<span class="label-text text-white">Artist</span>
								</label>
								<input
									type="text"
									placeholder="Enter artist name"
									class="input w-full max-w-xs"
									v-model="newSong.artist" required
								>
							</div>

							<div>
								<label class="label">
									<span class="label-text text-white">Photo</span>
								</label>
								<input
									type="file"
									class="file-input w-full max-w-xs"
									@change="handleFileUpload"
									accept="image/*"
								>

								<label class="label">
									<span class="label-text text-white">Tab Photo</span>
								</label>
								<input
									type="file"
									class="file-input w-full max-w-xs"
									@change="handleTablatureUpload"
									accept="image/*"
								>
							</div>

							<div>
								<label class="label">
									<span class="label-text text-white">Difficulty Level</span>
								</label>
								<select v-model="newSong.difficulty_level" class="select w-full max-w-xs">
									<option value="easy">Easy</option>
									<option value="medium">Medium</option>
									<option value="hard">Hard</option>
								</select>

								<label class="label">
									<span class="label-text text-white">Genre</span>
								</label>
								<select v-model="newSong.genre" class="select w-full max-w-xs">
									<option value="rock">Rock</option>
									<option value="pop">Pop</option>
									<option value="hip-hop">Hip Hop</option>
								</select>
							</div>
						</div>


						<div class="flex justify-between items-end">
						<div class="">
						<label class="label">
							<span class="label-text text-white">Video Link</span>
						</label>
						<input
							type="text"
							placeholder="Enter video link"
							class="input w-full max-w-xs"
							v-model="newSong.video_link" required
						>
						</div>
						<div>
							<button class="btn btn-active btn-success mr-3" type="submit">+ Add</button>
							<a @click="toggleAddModal" class="btn btn-info">Close</a>
						</div>
					</div>
					</div>
				</form>
		</div>


		<ul class="flex flex-col">
			<li class="flex p-5 text-white glass mt-10 rounded-2xl justify-between items-center" v-for="song in filteredSongs" :key="song.id">
				<div class="flex">
					<div class="avatar">
						<div class="w-32 rounded">
							<img :src="song.photo" alt="image">
						</div>
					</div>

					<div class="ml-5">
						<h1 class="text-2xl">{{ song.title }}</h1>
						<h2 class="text-xl">by {{ song.artist }}</h2>
						<p>Genre: {{ song.genre }}</p>
						<p>Level: {{ song.difficulty_level }}</p>
					</div>
				</div>
				<div>
					<router-link class="btn btn-success mr-3" :to="{ name: 'songDetail', params: { slug: song.slug } }">
						Start
					</router-link>
					<button v-if="userData.user_type === 'teacher'" class="btn btn-error mr-3" @click="deleteSong(song.slug)">Delete</button>
				</div>
			</li>
		</ul>
	</div>
</template>

<script>
import axios from "axios";

export default {
	data() {
		return {
			userData: JSON.parse(localStorage.getItem('user_info')),
			songs: [],
			dateFilter: null,
			alphabeticalOrder: 'asc',
			genreFilter: '',
			difficultyFilter: '',
			searchQuery: '',
			imageUrl: '',
			isAddModalOpen: false,
			newSong: {
				title: '',
				artist: '',
				photo: null,
				difficulty_level: '',
				genre: '',
				tablature_photo: null,
				video_link: ''
			}
		};
	},
	computed: {
		genres() {
			return Array.from(new Set(this.songs.map(song => song.genre)));
		},
		difficultyLevels() {
			return Array.from(new Set(this.songs.map(song => song.difficulty_level)));
		},
		filteredSongs() {
			let filteredList = [...this.songs];

			if (this.genreFilter) {
				filteredList = filteredList.filter(song => song.genre === this.genreFilter);
			}

			if (this.difficultyFilter) {
				filteredList = filteredList.filter(song => song.difficulty_level === this.difficultyFilter);
			}

			if (this.searchQuery) {
				const searchQueryLower = this.searchQuery.toLowerCase();
				filteredList = filteredList.filter(
					song =>
						song.title.toLowerCase().includes(searchQueryLower) ||
						song.artist.toLowerCase().includes(searchQueryLower)
				);
			}

			if (this.alphabeticalOrder === 'asc') {
				filteredList.sort((a, b) => a.title.localeCompare(b.title));
			} else {
				filteredList.sort((a, b) => b.title.localeCompare(a.title));
			}

			return filteredList;
		},
	},
	methods: {
		toggleAddModal() {
			this.isAddModalOpen = !this.isAddModalOpen;
		},
		async fetchSongs() {
			try {
				const response = await axios.get('http://127.0.0.1:8000/api/songs/');
				this.songs = response.data;
			} catch (error) {
				console.error('Error fetching songs:', error);
			}
		},
		async deleteSong(songId) {
			if (confirm('Are you sure you want to delete this song?')) {
				try {
					await axios.delete(`http://127.0.0.1:8000/api/songs/${songId}/`);
					this.fetchSongs();
				} catch (error) {
					console.error('Error deleting song:', error);
				}
			}
		},
		filterSongs() {
			this.fetchSongs();
		},

		viewSongDetail(slug) {
			this.$router.push({ name: 'songDetail', params: { slug: slug } });
		},

		async addSong() {
			try {
				const response = await axios.post('http://127.0.0.1:8000/api/songs/', {
					title: this.newSong.title,
					artist: this.newSong.artist,
					photo: this.newSong.photo,
					tablature_photo: this.newSong.tablature_photo,
					difficulty_level: this.newSong.difficulty_level,
					genre: this.newSong.genre,
					video_link: this.newSong.video_link,
				},{
					headers: {
						'Content-Type': 'multipart/form-data',
					},
				});
				await this.fetchSongs()
				await this.toggleAddModal()
				console.log('Song added:', response.data);
			} catch (error) {
				console.error('Error adding song:', error);
			}
		},
		handleFileUpload(event) {
			this.newSong.photo = event.target.files[0];
		},

		handleTablatureUpload(event) {
			this.newSong.tablature_photo = event.target.files[0];
		},
	},
	mounted() {
		this.fetchSongs();
	},
};
</script>
