import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../Login/Login.css";
import logo from "../../assets/Images/logo.svg";

const Login = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ email: "", password: "" });
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    const form = new URLSearchParams();
    form.append("username", formData.email);
    form.append("password", formData.password);

    try {
      const response = await fetch("http://127.0.0.1:8000/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: form.toString(),
      });

      const data = await response.json();
      console.log("Ответ сервера:", data);

      if (!response.ok) {
        throw new Error(data.detail?.[0]?.msg || "Ошибка входа");
      }

      localStorage.setItem("token", data.access_token);
      console.log("token saved:", data.access_token);
      navigate("/profile");
    } catch (err) {
      console.error("Ошибка входа:", err);
      setError(err.message);
    }
  };

  return (
    <div className="container">
      <div className="logo">
        <img src={logo} alt="Логотип" />
      </div>
      <div className="title">Вход</div>
      <div className="form_box">
        <form className="form" onSubmit={handleSubmit}>
          <input
            type="email"
            name="email"
            placeholder="Email"
            className="input"
            value={formData.email}
            onChange={handleChange}
          />
          <input
            type="password"
            name="password"
            placeholder="Пароль"
            className="input"
            value={formData.password}
            onChange={handleChange}
          />
          <button type="submit" className="button">
            Войти
          </button>
        </form>
        {error && (
          <div style={{ color: "red", marginTop: "10px" }}>{error}</div>
        )}
        <div className="register_link">
          Нет аккаунта? <a href="/register">Зарегистрироваться</a>
        </div>
      </div>
    </div>
  );
};

export default Login;
