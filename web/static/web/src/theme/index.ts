import { createTheme, responsiveFontSizes } from "@mui/material";

const theme = createTheme({
  palette: {
    mode: "dark",
  },
  typography: {
    fontFamily: ['"Nunito Sans"', "Inter", "Avenir", "Helvetica", "Arial", "sans-serif"].join(", "),
    fontSize: 16,
  },
});

export default responsiveFontSizes(theme);
