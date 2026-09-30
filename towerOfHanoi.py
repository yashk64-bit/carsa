<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DriveX - Cars</title>

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Arial, sans-serif;
    }

    body {
      background: #f5f5f5;
      color: #222;
    }

    /* Navbar */
    nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px 8%;
      background: #111;
      color: white;
    }

    .logo {
      font-size: 28px;
      font-weight: bold;
      color: #ff3b30;
    }

    nav ul {
      display: flex;
      list-style: none;
      gap: 30px;
    }

    nav a {
      color: white;
      text-decoration: none;
    }

    /* Hero */
    .hero {
      min-height: 80vh;
      display: flex;
      align-items: center;
      justify-content: center;
      text-align: center;
      color: white;

      background:
        linear-gradient(rgba(0,0,0,.55), rgba(0,0,0,.55)),
        url("https://images.unsplash.com/photo-1503376780353-7e6692767b70")
        center/cover;
    }

    .hero h1 {
      font-size: 60px;
      margin-bottom: 15px;
    }

    .hero p {
      font-size: 20px;
      margin-bottom: 30px;
    }

    .btn {
      display: inline-block;
      padding: 14px 30px;
      background: #ff3b30;
      color: white;
      text-decoration: none;
      border-radius: 6px;
      font-weight: bold;
    }

    /* Cars */
    .cars {
      padding: 60px 8%;
      text-align: center;
    }

    .cars h2 {
      font-size: 36px;
      margin-bottom: 40px;
    }

    .car-container {
      display: flex;
      justify-content: center;
      gap: 25px;
      flex-wrap: wrap;
    }

    .car-card {
      width: 300px;
      background: white;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 5px 20px rgba(0,0,0,.1);
      transition: .3s;
    }

    .car-card:hover {
      transform: translateY(-8px);
    }

    .car-card img {
      width: 100%;
      height: 190px;
      object-fit: cover;
    }

    .car-info {
      padding: 20px;
      text-align: left;
    }

    .car-info h3 {
      margin-bottom: 10px;
    }

    .price {
      color: #ff3b30;
      font-weight: bold;
      margin-bottom: 15px;
    }

    /* Footer */
    footer {
      text-align: center;
      padding: 25px;
      background: #111;
      color: white;
    }

    @media (max-width: 600px) {
      .hero h1 {
        font-size: 40px;
      }

      nav ul {
        display: none;
      }
    }
  </style>
</head>

<body>

  <nav>
    <div class="logo">DriveX</div>

    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#cars">Cars</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>

  <section class="hero">
    <div>
      <h1>Drive Your Dream Car</h1>
      <p>Discover powerful, stylish and modern cars.</p>
      <a href="#cars" class="btn">Explore Cars</a>
    </div>
  </section>

  <section class="cars" id="cars">
    <h2>Featured Cars</h2>

    <div class="car-container">

      <div class="car-card">
        <img src="https://images.unsplash.com/photo-1494976388531-d1058494cdd8"
             alt="Sports car">

        <div class="car-info">
          <h3>Sport X</h3>
          <p class="price">$45,000</p>
          <p>Powerful performance with a modern design.</p>
        </div>
      </div>

      <div class="car-card">
        <img src="https://images.unsplash.com/photo-1553440569-bcc63803a83d"
             alt="Luxury car">

        <div class="car-info">
          <h3>Luxury Pro</h3>
          <p class="price">$65,000</p>
          <p>Luxury, comfort and advanced technology.</p>
        </div>
      </div>

      <div class="car-card">
        <img src="https://images.unsplash.com/photo-1542282088-72c9c27ed0cd"
             alt="Modern car">

        <div class="car-info">
          <h3>Urban GT</h3>
          <p class="price">$38,000</p>
          <p>Perfect combination of style and everyday performance.</p>
        </div>
      </div>

    </div>
  </section>

  <footer>
    <p>© 2026 DriveX. All rights reserved.</p>
  </footer>

</body>
</html>
