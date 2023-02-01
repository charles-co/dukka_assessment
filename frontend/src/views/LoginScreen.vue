<template>
    <FormSlider type="login" @formSubmitted="onFormSubmitted"/>
</template>


<script>
import FormSlider from '../components/FormSlider.vue';
import axiosInstance from '@/axios';

export default {
    name: 'LoginScreen',
    components: {
        FormSlider,
    },
    methods: {
        onFormSubmitted(event) {
            axiosInstance.post('/auth-token/', {
                email: event.data.email,
                password: event.data.password
            }).then(response => {
                if (response.status === 200){
                    localStorage.setItem('token', response.data.token);
                    this.$store.commit('setUserLoginStatus', true);
                    this.$router.push('/dashboard');
                }
                else {
                    this.$router.push('/login');
                }
            }).catch(error => {
                console.log(error);
            });
        }
    },
}
</script>
