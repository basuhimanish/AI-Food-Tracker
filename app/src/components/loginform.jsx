import { useState } from "react";
import api from "../api";
import "../css/loginpage.css";

export default function LoginForm({ setToggle, setLoggedin, setinfo }) {
  const [login, setLogin] = useState({
    email: "",
    password: "",
  });

  async function handlesubmit(e) {
    e.preventDefault();
    // api call

    try {
      const response = await api.post("/user/verify", login);
      console.log(response);
      if (response.data.status) {
        setLoggedin(true);
        setinfo({
          username: response.data.username,
          userid: response.data.userid,
        });
      }
    } catch (error) {
      console.error("Error Retrieving file from database: ", error);
    }
  }

  return (
    <div className="login_signup_card">
      <div className="p">Login</div>
      <br></br>
      <input
        className="input"
        type="text"
        placeholder="email"
        onChange={(e) => setLogin({ ...login, email: e.target.value })}
      ></input>
      <br></br>
      <input
        className="input"
        type="password"
        placeholder="password"
        onChange={(e) => setLogin({ ...login, password: e.target.value })}
      ></input>
      <br></br>
      <br></br>
      <button className="loginbtn" onClick={(e) => handlesubmit(e)}>
        Submit
      </button>
      <br></br>
      <button
        className="signupbtn"
        onClick={() => {
          setToggle(false);
        }}
      >
        {" "}
        New User? Sign-up{" "}
      </button>
    </div>
  );
}
