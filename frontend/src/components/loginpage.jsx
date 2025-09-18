import React, { useState } from "react";
import SignupForm from "./signupform";
import LoginForm from "./loginform";
import Dashboard from "./dashboard";

export default function Login() {
  const [toggle, setToggle] = useState(true);
  const [info, setinfo] = useState({ username: "", userid: "" });
  const [isloggedin, setLoggedin] = useState(false);

  if (isloggedin) {
    return <Dashboard info={info} />;
  }

  return (
    <>
      {toggle ? (
        <>
          <LoginForm
            setToggle={setToggle}
            setLoggedin={setLoggedin}
            setinfo={setinfo}
          />
        </>
      ) : (
        <>
          <SignupForm setToggle={setToggle} />
        </>
      )}
    </>
  );
}
