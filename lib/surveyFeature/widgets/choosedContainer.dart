import 'package:flutter/cupertino.dart';

class Choosedcontainer extends StatelessWidget {
  final String txt;
  const Choosedcontainer({super.key,required this.txt});

  @override
  Widget build(BuildContext context) {
    return  Container(
      width: 102,
      height: 52,
      decoration:BoxDecoration(
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color:const  Color(0xff207344))
      ),
      child: Center(
        child:Text(txt,
        style:const TextStyle(
          color: Color(0xffABABAB),
        ),
        ),
      ),
    );
  }
}
