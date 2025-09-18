import { useState } from "react";
import api from "../api";

export default function SignupForm({ setToggle }) {
  const [signup, setsignup] = useState({
    name: "",
    email: "",
    password: "",
  });

  const [error, setErrorMessage] = useState({ status: false, message: "" });
  const [isAccountCreated, setAccountCreated] = useState(false);

  async function handlesubmit(e) {
    e.preventDefault();

    try {
      const response = await api.post("/user/add", signup);
      console.log(response);

      if (response.data.status) {
        setAccountCreated(true);
      } else {
        setErrorMessage({ status: true, message: response.data.message });
      }
    } catch (error) {
      console.log(error);
    }
  }

  function close() {
    setErrorMessage({ status: false, message: "" });
  }

  return (
    <>
      <div className="login_signup_card">
        <div className="p">Sign-Up</div>
        <br></br>
        <input
          className="input"
          type="text"
          placeholder="name"
          onChange={(e) => setsignup({ ...signup, name: e.target.value })}
        ></input>
        <br></br>
        <input
          className="input"
          type="text"
          placeholder="email"
          onChange={(e) => setsignup({ ...signup, email: e.target.value })}
        ></input>
        <br></br>
        <input
          className="input"
          type="password"
          placeholder="password"
          onChange={(e) => setsignup({ ...signup, password: e.target.value })}
        ></input>
        <br></br>
        <br></br>
        <button className="loginbtn" onClick={(e) => handlesubmit(e)}>
          {" "}
          Submit{" "}
        </button>
        <br></br>
        <button
          className="signupbtn"
          onClick={() => {
            setToggle(true);
          }}
        >
          Already a user? Login.
        </button>
      </div>

      <div className={`errorCard ${error.status ? "show" : ""}`}>
        <div className="errorMessage">
          Error
          <br></br>
          {error.message}
        </div>
        <button className="crossbtn" onClick={() => close()}>
          <img src="../../icons/loginpage/cross.png" className="cross"></img>
        </button>
      </div>

      <div className={`createdCard ${isAccountCreated ? "show" : ""}`}>
        <div className="errorMessage">
          Account Created Successfully
          <br></br>
          Go to Login-Page
        </div>
        <button className="crossbtn" onClick={() => close()}>
          <img src="../../icons/loginpage/cross.png" className="cross"></img>
        </button>
      </div>
    </>
  );
}
