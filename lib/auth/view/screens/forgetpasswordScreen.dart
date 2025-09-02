import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:tester/auth/view/widgets/mainButton.dart';
import 'package:tester/auth/view/widgets/maintxt.dart';
import 'package:tester/auth/view/widgets/subheadtxt.dart';

import '../widgets/txtfield.dart';

class Forgetpasswordscreen extends StatelessWidget {
  const Forgetpasswordscreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SingleChildScrollView(
        child: Padding(padding:  const EdgeInsets.symmetric(horizontal: 24),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              SizedBox(height: 230,),
              const Maintxt(txt: 'Forget Password'),
              const SizedBox(height: 24,),
              const Subheadtxt(txt: 'Enter your email to reset \n your password'),
              const SizedBox(height: 34,),
              const CustomTextField(labelText: 'Enter your Email', icona: Icons.email,),
              const SizedBox(height: 50,),
              Mainbutton(func: (){}, txt: 'Send Code'),
            ],
          ),
        ),
      ),
    );
  }
}
