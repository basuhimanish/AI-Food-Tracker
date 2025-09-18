import React, { useState } from "react";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

import api from "../api";
import NavigationBar from "./navbar";
import "../css/dashboard.css";

export default function Dashboard({ info }) {
  const [sendData, setsendData] = useState({
    expiry_date: "",
    userid: info.userid,
  });

  const [isFormVisible, setFormVisible] = useState(false);
  const [isCalendarOpen, setIsCalendarOpen] = useState(true);

  async function scan_barcode(e) {
    e.preventDefault();

    try {
      const response = await api.post("/item/scan", sendData);
      console.log(response);
    } catch (error) {
      console.log("Error", error);
    }

    setFormVisible(false);
    setsendData({ ...sendData, expiry_date: "" });
  }

  return (
    <div>
      <div className="pagetop">
        <NavigationBar />
        <div className="bgimagewrapper">
          <div className="bgimage"></div>
        </div>
        <h1 className="welcome"> Welcome {info.username}</h1>

        <div className="container">
          <div className="item1">
            <button className="cardbtn">
              <img
                className="cardimg"
                src="../../icons/dashboard/inventory.png"
              ></img>
            </button>
          </div>

          <div className="item2">
            <button className="cardbtn">
              <img
                className="cardimg"
                src="../../icons/dashboard/recipe.png"
              ></img>
            </button>
          </div>

          <div className="item3">
            <button className="cardbtn">
              <img
                className="cardimg"
                src="../../icons/dashboard/donation.png"
              ></img>
            </button>
          </div>

          <div className="item4">
            <button className="cardbtn">
              <img
                className="cardimg"
                src="../../icons/dashboard/profile.png"
              ></img>
            </button>
          </div>

          <div className="item5">
            {!isFormVisible && (
              <div>
                <button
                  className="cardbtn"
                  onClick={() => setFormVisible(true)}
                >
                  <img
                    className="cardimg"
                    src="../../icons/dashboard/camera.png"
                  ></img>
                </button>
              </div>
            )}

            {isFormVisible && (
              <div className="datepicker">
                <DatePicker
                  selected={
                    sendData.expiry_date ? new Date(sendData.expiry_date) : null
                  }
                  onChange={(date) => {
                    const yyyy = date.getFullYear();
                    const mm = String(date.getMonth() + 1).padStart(2, "0");
                    const dd = String(date.getDate()).padStart(2, "0");
                    const formattedDate = `${yyyy}-${mm}-${dd}`;
                    setsendData({ ...sendData, expiry_date: formattedDate });
                    setIsCalendarOpen(false);
                  }}
                  dateFormat="yyyy-MM-dd"
                  placeholderText="Select Date"
                  className="cardtext"
                  open={isCalendarOpen}
                  onClickOutside={() => setIsCalendarOpen(false)}
                  onSelect={() => setIsCalendarOpen(false)}
                  onFocus={() => setIsCalendarOpen(true)}
                />

                <br />
                <button
                  className="btn"
                  onClick={(e) => scan_barcode(e)}
                  onClickOutside={() => setFormVisible(false)}
                >
                  {" "}
                  Scan Barcode{" "}
                </button>
              </div>
            )}
          </div>
        </div>
      </div>

      <div className="pagebottom"></div>
    </div>
  );
}
