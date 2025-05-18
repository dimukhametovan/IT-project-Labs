import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../Register/Register.css";
import logo from "../../assets/Images/logo.svg";
import api from "../../api/axios.js";

const Register = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

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

    if (formData.password !== formData.confirmPassword) {
      setError("Пароли не совпадают");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          full_name: formData.full_name,
          email: formData.email,
          password: formData.password,
          confirm_password: formData.confirmPassword,
        }),
      });

      if (!response.ok) {
        const data = await response.json();
        console.error("Server response:", data);

        if (Array.isArray(data.detail)) {
          // если detail — массив ошибок
          const messages = data.detail.map((err) => err.msg).join(", ");
          setError(messages);
        } else {
          setError(data.detail || data.message || "Ошибка регистрации");
        }

        return;
      }

      navigate("/");
    } catch (err) {
      setError("Ошибка подключения к серверу");
    }
  };

  return (
    <div className="container">
      <div className="logo">
        <img src={logo} alt="Логотип" />
      </div>
      <div className="title">Регистрация</div>

      <div className="form_box">
        <form className="form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="full_name"
            placeholder="Ф.И.О."
            className="input"
            value={formData.full_name}
            onChange={handleChange}
            required
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            className="input"
            value={formData.email}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="password"
            placeholder="Пароль"
            className="input"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <input
            type="password"
            name="confirmPassword"
            placeholder="Подтверждение пароля"
            className="input"
            value={formData.confirmPassword}
            onChange={handleChange}
            required
          />
          <button type="submit" className="button">
            Зарегистрироваться
          </button>
        </form>

        {error && <div style={{ color: "red", marginTop: 10 }}>{error}</div>}

        <div className="login_link">
          Уже зарегистрированы? <a href="/">Войти</a>
        </div>
      </div>
    </div>
  );
};

export default Register;
