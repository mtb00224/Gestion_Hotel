import React from 'react';
import 'react-native-gesture-handler';
import {StatusBar} from 'react-native';
import {NavigationContainer} from '@react-navigation/native';
import HomeScreen from './src/views/screens/HomeScreen';
import BookScreen from './src/views/screens/BookScreen';
import ChambresScreen from './src/views/screens/ChambresScreen';
import ReservationScreen from './src/ReservationScreen';
import AddReservationScreen from './src/views/screens/AddReservationScreen';
import COLORS from './src/consts/colors';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import DetailsScreen from './src/views/screens/DetailsScreen';
import ChooseTarifScreen from './src/views/screens/ChooseTarifScreen';
import ListeResrvationScreen from './src/views/screens/ListeReservation';

const Stack = createNativeStackNavigator();
const App = () => {
  return (
    <NavigationContainer>
      <StatusBar backgroundColor={COLORS.white} barStyle="dark-content" />
      <Stack.Navigator screenOptions={{headerShown: false}}>
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="DetailsScreen" component={DetailsScreen} />
          <Stack.Screen name="book" component={BookScreen} /> 
          <Stack.Screen name="Chambres" component={ChambresScreen} />
          <Stack.Screen name="Reservations" component={ReservationScreen} />
          <Stack.Screen name="AddReservation" component={AddReservationScreen} />
          <Stack.Screen name="tarif" component={ChooseTarifScreen} />
          <Stack.Screen name="List" component={ListeResrvationScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default App;
