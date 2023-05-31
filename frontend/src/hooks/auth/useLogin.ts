import { authService } from "../../services";
import Cookies from "js-cookie";
import { UserToken, LoginForm } from "../../services/auth.service";
import { time } from "console";

export const useLogin = () => {
  const login = async (input : LoginForm) => {
    console.log('starting request')
    const user = await authService.login(input);
    console.log('ended request request')
    if (user) {
      Cookies.set("currentUser", JSON.stringify(user));
    }
    return user as UserToken;
  };

  return { login };
};