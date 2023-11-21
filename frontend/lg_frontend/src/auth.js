import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/';
const axiosInstance = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

const login = async (email, password) => {
    try {
        const response = await axios.post(`${API_URL}token/`, {
            email: email,
            password: password,
        });

        if (response.status === 200) {
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
            return response.data;
        } else {
            throw Error('Неверный статус ответа при аутентификации');
        }
    } catch (error) {
        console.log(error)
    }
};

export const getUserInfo = async () => {
    try {
        const response = await axiosInstance.get('user/');
        localStorage.setItem('user_info', JSON.stringify(response.data));
        return response.data;
    } catch (error) {
        console.error('Ошибка при получении информации о пользователе:', error);
        throw error;
    }
};


axiosInstance.interceptors.request.use(
    (config) => {
        const access_token = localStorage.getItem('access_token');
        if (access_token) {
            config.headers['Authorization'] = `Bearer ${access_token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export {login, axiosInstance};
