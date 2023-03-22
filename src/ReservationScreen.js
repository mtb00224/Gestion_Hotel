
import { StyleSheet,Text,TouchableOpacity,SafeAreaView } from 'react-native';
import React, { useState,useEffect } from 'react-native';
import COLORS from './consts/colors';
import Slider from './views/screens/Slider';
const  ReservationScreen=({ navigation }) =>
{


  // const [Data,setData]=useState([])
      
  const image = [
    'https://assets.hotelaparis.com/uploads/pictures/000/043/953/Chambre-3-6.jpg',
    'https://www.yonder.fr/sites/default/files/styles/lg-insert/public/contenu/destinations/5%20Codet%20chambre%20%C2%A9%20Antoine%20Schramm_0.jpg?itok=jv3m9LdX',
    'https://www.lyon-entreprises.com/wp-content/uploads/2022/05/img-chambres-decorer-points-1024x683.jpg',
  ];

  //  useEffect(()=>{
  //   fetch('http://localhost:8000/Reservation')
  //      .then(res=>{
  //         return res.json()
  //      })
  //      .then(data=>{
  //         setData(data)
  //      })
  //      .catch(err=>{
  //       console.log(err)
  //      })

  //  },[])

    
      
    

  return (
    <SafeAreaView >
      <Text style={style.text}>Reservations managings</Text>
      <TouchableOpacity
        style={style.button}
         onPress={() => navigation.navigate('AddReservation')}
      >
        <Text style={style.buttonText}>Add Reservation</Text>
      </TouchableOpacity>
      <TouchableOpacity
        style={style.button}
        onPress={() => navigation.navigate('List')}
      >
        <Text style={style.buttonText}>List Reservation</Text>

      </TouchableOpacity>

    
      
      <Slider images={image}  />
    </SafeAreaView>
    
  );
}


const style = StyleSheet.create({
    header: {
      marginTop: 25,
      flexDirection: 'row',
      justifyContent: 'space-between',
      paddingHorizontal: 20,
    },
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
    },
    text: {
      fontSize: 24,
      marginTop:12,
      marginLeft:15
    },
    button: {
      backgroundColor:  COLORS.primary,
      padding: 10,
      borderRadius: 5,
      marginBottom: 20,
      marginTop:35
    },
    buttonText: {
      color: '#ffffff',
      fontSize: 18,
    },
  
  })

export default ReservationScreen