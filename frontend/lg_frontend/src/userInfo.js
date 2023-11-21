import { reactive } from 'vue';
import { getUserInfo } from '@/auth.js';

export const userInfo = reactive({
    data: null,
    async fetchData() {
        try {
            const response = await getUserInfo();
            this.data = response;
            localStorage.setItem('user_info', response);
        } catch (error) {
            console.error('Failed to fetch user info', error);
        }
    },
});
