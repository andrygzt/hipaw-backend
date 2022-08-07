import React from "react";
import PropTypes from "prop-types";
import { withStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import RadioGroup from "@material-ui/core/RadioGroup";
import Radio from "@material-ui/core/Radio";
import Grid from "@material-ui/core/Grid";
import FormControl from "@material-ui/core/FormControl";
import FormLabel from "@material-ui/core/FormLabel";
import FormControlLabel from "@material-ui/core/FormControlLabel";
import FormGroup from "@material-ui/core/FormGroup";
import Checkbox from "@material-ui/core/Checkbox";

const styles = ({ breakpoints }) => ({
  root: {
    padding: 16,
    [breakpoints.up("sm")]: {
      padding: 24,
      maxWidth: 500,
      margin: "auto",
    },
    [breakpoints.up("md")]: {
      maxWidth: 700,
    },
  },
  paper: {
    padding: 16,
  },
});

const ContentForm = ({
  classes,
  preset,
  onChangePreset,
  data,
  onChangeData,
}) => {
  const handleChange = (key) => (e) =>
    onChangeData({
      ...data,
      [key]: e.target.checked,
    });
  return (
    <div className={classes.root}>
      <Paper elevation={1} square className={classes.paper}>
        <Grid container>
          <Grid item xs={6}>
            <FormControl component="fieldset">
              <FormLabel component="legend">Post</FormLabel>
            </FormControl>
          </Grid>
          <Grid item xs={6}></Grid>
        </Grid>
      </Paper>
    </div>
  );
};

ContentForm.propTypes = {
  classes: PropTypes.shape({}).isRequired,
  preset: PropTypes.string.isRequired,
  onChangePreset: PropTypes.func.isRequired,
  data: PropTypes.shape({}).isRequired,
  onChangeData: PropTypes.func.isRequired,
};
ContentForm.defaultProps = {};

export default withStyles(styles)(ContentForm);
