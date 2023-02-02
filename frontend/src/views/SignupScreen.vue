<template>
    <FormSlider type="signup" @formSubmitted="onFormSubmitted"/>
</template>

<script>
import FormSlider from '../components/FormSlider.vue';
import axiosInstance from '@/axios';

export default {
    name: 'SignupScreen',
    components: {
        FormSlider,
    },
    methods: {
        onFormSubmitted(event) {
            axiosInstance.post('/api/v1/users/', {
                "email": event.data.email,
                "password": event.data.password,
                "password2": event.data.password2,
                "name": event.data.name,
                "sex": event.data.sex,
                "country": event.data.country,
                "phone_number": event.data.phone_number,
            }).then(response => {
                if (response.status === 201){
                    axiosInstance.post('/auth-token/', {
                        email: event.data.email,
                        password: event.data.password
                    }).then(response => {
                        localStorage.setItem('token', response.data.token);
                        this.$store.commit('setUserLoginStatus', true);
                        this.$router.push('/dashboard');
                    }).catch(error => {
                        console.log(error);
                    });
                }
                else {
                    this.$router.push('/signup');
                }
            }).catch(() => {
                this.$router.push('/signup');
            });
        }
    },
}
</script>
