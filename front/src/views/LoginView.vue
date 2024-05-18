<template>
  <div>
    <h1>Вход</h1>
    <v-form @submit.prevent>
      <v-text-field v-model="user.email" label="Email"></v-text-field>
      <v-text-field v-model="user.pwd" label="Пароль"></v-text-field>
      <v-btn class="mt-2" type="submit" block @click="send">Регистрация</v-btn>
    </v-form>
  </div>
</template>


<script>
export default {
  methods: {
    send() {
      this.axios.post("http://127.0.0.1:8000/login", this.user).then(response => {
        console.log(response)
        localStorage.setItem('JWT_token', response.data.token)
        localStorage.setItem('exp', response.data.exp)
        this.$toast.open({
          message: 'Вход успешн',
          type: 'success',
        });
      }).catch(data => {
        console.log(data)
        this.$toast.open({
          message: 'Ошибка валидации',
          type: 'error',
        });
      })

    }
  },
  data: () => ({
    user: {
      email: null,
      pwd: null,
    }
  }),
}
</script>
