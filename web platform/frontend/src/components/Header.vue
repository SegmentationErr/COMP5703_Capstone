<template>
  <div id="header">
    <div class="nav-container">
      <div class="flex">
        <div class="flex-left">
          <a class="navbar-brand nav-link" href="/">
<!--            <img class="brand-logo" src="https://bigquant.com/static/img/logo-bigquant.png">-->
            <span>LOGO HERE</span>
          </a>
        </div>
        <div class="flex-right">
          <ul class="nav navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="/">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/">Introduction</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/">Github</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Header'
}
</script>

<style scoped>
#header {
  z-index: 99;
  position: fixed;
  top: 0;
  right: 0;
  left: 0;
  background-color: #e74c3c;
  font-size: 16px;
}

.nav-container {
  padding: 0 2rem 0 2rem;

}

.flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.flex-left {

}

.navbar-nav {
  display: flex;
}

.navbar-brand .brand-logo {
  height: 36px;
}

li {
  list-style-type: none;
  padding: 0 15px;
}

.nav-link {
  color: #fff;
  display: block;
  text-decoration: none;
}

.dropdown {
  display: flex;
  align-items: center;
}

.dropdown:after {
  margin-left: 3px;
  width: 0;
  height: 0;
  content: "";
  border-top: 5px solid white;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  display: inline-block;
}

</style>
