// import "./App.css";
import { useState } from "react";
import NonUserHeader from "./components/NonUserHeader";
import UserHeader from "./components/UserHeader";
import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import IconButton from "@mui/material/IconButton";
import MenuIcon from "@mui/icons-material/Menu";
import { Button } from "@mui/material";
import "@fontsource/roboto/300.css";
function App() {
  const [headerDisplay, setHeaderDisplay] = useState(null);

  const toggleHeaderDisplay = () => {
    if (headerDisplay) {
      return (
        <NonUserHeader
          user_id={headerDisplay}
          changeHeaderCallback={setHeaderDisplay}
        />
      );
    } else {
      return <UserHeader changeHeaderCallback={setHeaderDisplay} />;
    }
  };
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar variant="regular">
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 3 }}
          >
            <MenuIcon />
          </IconButton>
          <Typography
            variant="h5"
            color="inherit"
            component="div"
            sx={{ flexGrow: 1 }}
            fontWeight="bold"
          >
            Welcome to Hi-Paw 🐾
          </Typography>
          <Button>
            <Typography color="white" variant="h6" component="div">
              Login
            </Typography>
          </Button>
        </Toolbar>
      </AppBar>
    </Box>
  );
}

export default App;
